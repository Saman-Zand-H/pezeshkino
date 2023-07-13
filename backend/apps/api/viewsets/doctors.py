from django.db.models import Q
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser

from api.permissions import IsSuperuser
from doctors.models import (Doctor, 
                            DoctorOffice,
                            AvailabilityTime,
                            AvailabilityDay)
from api.serializers.doctors import (DoctorSerializer,
                                     DoctorOfficeSerializer,
                                     AvailabilityDaySerializer,
                                     AvailabilityTimeSerializer)
from api.paginations import DoctorsListPagination


# todo: manage permissions!!!!!
class DoctorViewset(ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsSuperuser]
    pagination_class = DoctorsListPagination
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "user__username"
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["user__last_name", 
                     "user__first_name", 
                     "user__username", 
                     "specialty"]
    
    def get_queryset(self):
        qs = super().get_queryset()
        city = self.request.query_params.get("city")
        specialty = self.request.query_params.get("specialty")
        search = self.request.query_params.get("search")
        if city:
            qs = qs.filter(doctor_offices__city=city)
        if specialty:
            qs = qs.filter(specialty=specialty)
        if search:
            qs = qs.filter(
                Q(user__first_name__contains=search)
                | Q(user__last_name__contains=search)
            )
        return qs
    
    def list(self, request, *args, **kwargs):
        ord_mapping = {"a": "", "d": "-"}
        name_order = request.GET.get("name_order")
        if name_order and (name_order:=name_order[0].lower()) in ["a", "d"]:
            order = ord_mapping[name_order]
            self.queryset = self.queryset.order_by(order+"user__last_name")
        return super().list(request, *args, **kwargs)
        

class DoctorOfficeViewset(ModelViewSet):
    serializer_class = DoctorOfficeSerializer
    queryset = DoctorOffice.objects.all()
    
    
class AvailabilityTimeViewset(ModelViewSet):
    serializer_class = AvailabilityTimeSerializer
    queryset = AvailabilityTime.objects.all()
    
    
class AvailabilityDayViewset(ModelViewSet):
    serializer_class = AvailabilityDaySerializer
    queryset = AvailabilityDay.objects.all()
    