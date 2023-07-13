from django.db import models
from django.conf import settings
from django.utils import timezone
from iranian_cities.fields import CityField
from django.contrib.gis.geos.point import Point
from django.core.exceptions import ValidationError
from django_jalali.db.models import jDateTimeField
from django.contrib.gis.db import models as gis_models
from phonenumber_field.modelfields import PhoneNumberField

from .enums import (Specialties, 
                    DaysOfWeek)


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="user_doctor",
                                on_delete=models.CASCADE)
    bio = models.TextField()
    specialty = models.CharField(choices=Specialties.choices, 
                                 max_length=5)
    visit_cost = models.IntegerField(default=20_000, blank=True, null=True)
    upin = models.CharField(max_length=20)
    verified = models.BooleanField(default=False)
    created_at = jDateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.name


class DoctorOffice(gis_models.Model):
    city = CityField(on_delete=models.SET_NULL,
                     null=True,
                     related_name="city_offices")
    address = models.CharField(max_length=200)
    office_title = models.CharField(max_length=40, default="default")
    consultation_fee = models.IntegerField(default=50_000)
    location = gis_models.PointField(default=Point(-180.0, -90.0))
    phonenumber = PhoneNumberField()
    doctor = models.ForeignKey(Doctor,
                               on_delete=models.CASCADE,
                               related_name="doctor_offices")
    created_at = jDateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.doctor.user.name}: {self.address}"
    
 
class AvailabilityDay(models.Model):
    office = models.ForeignKey(DoctorOffice,
                               on_delete=models.CASCADE,
                               related_name="office_availability")
    day_of_week = models.SmallIntegerField(choices=DaysOfWeek.choices)
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = [
            ["office", "day_of_week"]
        ]

    @property
    def doctor(self):
        return self.office.doctor

    def __str__(self):
        return f"{self.doctor} : {self.get_day_of_week_display()}"
    

class AvailabilityTime(models.Model):
    day = models.ForeignKey(AvailabilityDay,
                            on_delete=models.CASCADE,
                            related_name="availability_time")
    time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = [
            ["day", "time"]
        ]

    @property
    def doctor(self):
        return self.day.doctor

    def __str__(self):
        return f"{self.day} : {self.time}"
    