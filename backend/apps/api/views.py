from datetime import datetime
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import (get_earliest_available_appointment, 
                    get_available_times_in_range, 
                    check_availability)
from doctors.enums import Specialties
from appointments.models import Appointment
from doctors.models import AvailabilityTime
from .serializers.doctors import OfficeIdSerializer, MakeAppointmentSerializer
from .serializers.appointments import AppointmentSerializer


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
                "day": earliest.day.get_day_of_week_display(),
                "time": earliest.time
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


class MakeAppointmentView(APIView):
    def post(self, request, format=None):
        if not request.user.is_authenticated:
            return Response({"message": "you need to authenticated."},
                            status=status.HTTP_403_FORBIDDEN)
        
        data = MakeAppointmentSerializer(data=request.data)
        if not data.is_valid():
            return Response({"message": data.error_messages},
                            status=status.HTTP_400_BAD_REQUEST)
            
        office_id = data.validated_data.get("office_id")
        datetime_obj: datetime = data.validated_data.get("datetime")
        
        if not check_availability(office_id, datetime_obj):
            return Response({"message": "this time is not available for appointemnt."},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        
        availablity_time_obj = AvailabilityTime.objects.get(time=datetime_obj.time())
        appointment = Appointment.objects.create(patient=request.user,
                                                 office=office_id,
                                                 time=availablity_time_obj,
                                                 datetime=datetime_obj)
        return Response({"message": "the creation was successful.",
                         "appointment": AppointmentSerializer(appointment)},
                        status=status.HTTP_201_CREATED)        
