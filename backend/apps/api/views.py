import requests
from datetime import datetime
from logging import getLogger
from django.conf import settings
from rest_framework import status
from django.utils import timezone
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .exceptions import BankGatewayError
from .utils import (get_earliest_available_appointment, 
                    get_available_times_in_range, 
                    check_availability)
from .permissions import IsDoctor
from doctors.enums import Specialties
from payments.enums import PaymentStatus, Currencies
from doctors.models import (AvailabilityTime, 
                            AvailabilityDay, 
                            DoctorOffice,
                            Doctor)
from payments.models import MonetaryTransaction
from appointments.models import Appointment
from .serializers.users import (CustomRegisterSerializer, 
                                CustomTokenObtainPairSerializer)
from .serializers.payments import (TrackIdSerializer, 
                                   TransactionSerializer)
from .serializers.doctors import (OfficeIdSerializer, 
                                  DoctorOfficeSerializer,
                                  MakeAppointmentSerializer,
                                  ReviewSerializer,
                                  RegisterDoctorSerializer)
from .serializers.appointments import AppointmentSerializer
from doctors.queries import (get_revenues_for_last_week,
                             get_number_of_appointments_for_day, 
                             get_total_number_of_patients)


logger = getLogger(__name__)


class ListSpecialtiesView(APIView):
    def get(self, request, format=None):
        specs = [
            {
                "display_name": i.label,
                "code_name": i.value
            }
            for i in Specialties
        ]
        return Response(data=specs, 
                        status=status.HTTP_200_OK)
        

class GetEarliestFreeTimeView(APIView):
    def post(self, request, format=None):
        data = OfficeIdSerializer(data=request.data)
        
        if data.is_valid():
            office_id = data.validated_data.get("office_id")
            earliest = get_earliest_available_appointment(office_id)
            results = {
                "day": earliest["obj"].day.get_day_of_week_display(),
                "time": earliest["obj"].time
            }
            return Response(results, status=status.HTTP_200_OK)
        return Response({"message": data.errors}, status=status.HTTP_400_BAD_REQUEST)


class GetFreeTimesView(APIView):
    def post(self, request, format=None):
        data = OfficeIdSerializer(data=request.data)
        
        if data.is_valid():
            office_id = data.validated_data.get("office_id")
            # todo: try reduce time complexity in here
            times = []
            for i in get_available_times_in_range(office_id):
                for j in i["obj"].all():
                    times.append({
                        "get_day_of_week_display": j.day.get_day_of_week_display(),
                        "time": j.time,
                        "date": i["date"]
                    })
            return Response(times, status=status.HTTP_200_OK)
        return Response({"message": data.errors}, status=status.HTTP_400_BAD_REQUEST)


class InitiateAppointmentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):        
        data = MakeAppointmentSerializer(data=request.data)
        if not data.is_valid():
            return Response({"message": data.errors, },
                            status=status.HTTP_400_BAD_REQUEST)
            
        office_id = data.validated_data.get("office_id")
        office = DoctorOffice.objects.get(id=office_id)
        datetime_obj: datetime = data.validated_data.get("datetime")
        
        if not check_availability(office_id, datetime_obj):
            return Response({"message": "this time is not available for appointment."},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        
        availability_day_obj = AvailabilityDay.objects.get(office=office_id, 
                                                           day_of_week=datetime_obj.isoweekday())
        availability_time_obj = AvailabilityTime.objects.get(time=datetime_obj.time(), 
                                                             day=availability_day_obj)
        
        try:
            with transaction.atomic():
                appointment = Appointment.objects.create(patient=request.user,
                                                        office=office,
                                                        time=availability_time_obj,
                                                        datetime=datetime_obj)
                
                zibal_request_url = "https://gateway.zibal.ir/v1/request/"
                zibal_data = {
                    "merchant": getattr(settings, "ZIBAL_MERCHANT", "zibal"),
                    "amount": Currencies.toman_to_rial(office.consultation_fee),
                    "orderId": appointment.uuid.hex,
                    "callbackUrl": "http://localhost:8080/payment_status"
                }
                bank_response = requests.post(zibal_request_url, json=zibal_data)
                
                if bank_response.status_code != 200:
                    raise BankGatewayError({"response": bank_response.json(),
                                            "request": zibal_data})
        except BankGatewayError as e:
            logger.error(
                f"a problem at zibal gateway: {e}"
            )
            return Response({"message": "there's a problem with the gateway."},
                            status=status.HTTP_502_BAD_GATEWAY)
                
            
        trackId = bank_response.json().get("trackId")
        monetary_transaction = MonetaryTransaction.objects.create(
            by_user=request.user,
            for_user=office.doctor.user,
            amount=office.consultation_fee,
            currency=Currencies.IRT,
            trackId=trackId,
            status=PaymentStatus.Pending
        )
        appointment.transaction = monetary_transaction
        appointment.save()
        
        return Response({"message": "appointment was created successfully.",
                         "payLink": f"https://gateway.zibal.ir/start/{trackId}/"},
                        status=status.HTTP_200_OK)        


class PatientAppointmentsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        appointments = request.user.appointments.paid_appointments.all()
        data = AppointmentSerializer(appointments, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class DoctorAppointmentsView(APIView, PageNumberPagination):
    permission_classes = [IsDoctor]
    page_size = 20

    def get(self, request, format=None):
        appointments = Appointment.paid_appointments.filter(
            office__doctor__user=request.user)
        paginated_result = self.paginate_queryset(appointments, request, view=self)
        data = AppointmentSerializer(paginated_result, many=True).data
        return self.get_paginated_response(data)


class ValidateTransactionView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        data = TrackIdSerializer(data=request.data)
        
        if not data.is_valid():
            return Response({"message": data.errors},
                            status=status.HTTP_400_BAD_REQUEST)
            
        logger.critical(data.data)
        
        trackId = data.validated_data.get("trackId")
        transaction_qs = MonetaryTransaction.objects.filter(trackId=trackId)

        zibal_verify_url = "https://gateway.zibal.ir/v1/verify/"
        verify_data = {
            "merchant": getattr(settings, "ZIBAL_MERCHANT", "zibal"),
            "trackId": trackId
        }
        response = requests.post(zibal_verify_url, json=verify_data)
            
        if response.status_code != 200:
            logger.critical(response.request.body)
            return Response({"message": "there's a problem with the gateway."},
                            status=status.HTTP_502_BAD_GATEWAY)
        
        response_data = response.json()
        result_status = response_data.get("result")
        logger.critical(result_status)
        
        if result_status == 201:
            zibal_inquiry_url = "https://gateway.zibal.ir/v1/inquiry/"
            response = requests.post(zibal_inquiry_url, json=verify_data)
            response_data = response.json()
            result_status = response_data.get("result")
            
        if result_status == 100:
            transaction_qs.update(
                payment_time= response_data.get("paidAt"),
                reference_number= response_data.get("refNumber"),
                status= PaymentStatus.Complete,
                extra_information= response_data.get("description"),
                response_result= response_data.get("message")
            )
            return Response(TransactionSerializer(transaction_qs.last()).data,
                            status=status.HTTP_200_OK)
        
        # this transaction and appointment is redundant, so we delete it.
        transaction_qs.delete()
        return Response({"message": response_data.get("message")},
                        status=status.HTTP_400_BAD_REQUEST)
        

class ListByTransactionsView(APIView):
    def get(self, request, format=None):
        return Response(TransactionSerializer(request.user.by_transactions.all(), many=True))

class ListForTransactionsView(APIView):
    def get(self, request, format=None):
        return Response(TransactionSerializer(request.user.for_transactions.all(), many=True))


class ReviewView(APIView):
    def post(self, request, format=None):
        if not request.user.is_authenticated:
            return Response({"message": "you must be authenticated."},
                            status=status.HTTP_403_FORBIDDEN)
            
        data = ReviewSerializer(data=request.data)
        
        if not data.is_valid():
            return Response({"message": data.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        
        instance = data.save(by_user=request.user)
        return Response(ReviewSerializer(instance).data,
                        status=status.HTTP_201_CREATED)
        
    def get(self, request, format=None):
        doctor_username = str(request.GET.get("doctor_username"))
        doctor_qs = Doctor.objects.filter(user__username=doctor_username)
        
        if not doctor_qs.exists():
            return Response({"doctor_username": "no doctor with this username exists."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        doctor = doctor_qs.last()
        reviews = doctor.doctor_reviews.all()
        return Response(ReviewSerializer(reviews, many=True).data,
                        status=status.HTTP_200_OK)
        
    
class RegisterDoctorView(APIView):
    def post(self, request, fromat=None):
        data = RegisterDoctorSerializer(data=request.data)
        
        if not data.is_valid():
            return Response(data.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        upin = data.validated_data.pop("upin")
        request.data.pop("upin")
        specialty = data.validated_data.pop("specialty")
        request.data.pop("specialty")
        
        try:
            user = data.save(request=request)
            Doctor.objects.create(user=user,
                                    specialty=specialty,
                                    upin=upin)
            response_data = {}
            refresh_token_obj = CustomTokenObtainPairSerializer.get_token(user)
            response_data.update({"refresh_token": str(refresh_token_obj),
                                    "access_token": str(refresh_token_obj.access_token),
                                    "user": CustomRegisterSerializer(data.validated_data).data})
            return Response(
                response_data, 
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            logger.critical(e)
            return Response({"message": "something went wrong. please reach us."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
class DashboardHomeDataView(APIView):
    permission_classes = [IsDoctor]
    
    def get(self, request, format=None):
        doctor = request.user.user_doctor
        doctor_id = doctor.id
        timestamp = timezone.now()
        data = {
            "number_of_patients": get_total_number_of_patients(
                doctor_id),
            "revenue_for_week": get_revenues_for_last_week(
                doctor_id, timestamp),
            "number_of_appointments": get_number_of_appointments_for_day(
                doctor_id, timestamp),
            "number_of_offices": doctor.doctor_offices.count(),
            "comments": ReviewSerializer(doctor.doctor_reviews.all()[:5], many=True).data
        }
        data["weekly_income"] = sum(i["income"] for i in data["revenue_for_week"])
        return Response(data, status=status.HTTP_200_OK)


class GetDoctorOfficesView(APIView):
    permission_classes = [IsDoctor]
    
    def get(self, request, format=None):
        doctor = request.user.user_doctor
        data = DoctorOfficeSerializer(doctor.doctor_offices.all(), many=True).data
        return Response(data, status=status.HTTP_200_OK)
