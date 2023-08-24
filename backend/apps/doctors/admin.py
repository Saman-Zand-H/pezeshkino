from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.admin.decorators import register

from .models import Doctor, DoctorOffice, AvailabilityDay, AvailabilityTime


@register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    ...


@register(DoctorOffice)
class DoctorOfficeAdmin(OSMGeoAdmin):
    list_display = ["city", "address", "doctor"]


@register(AvailabilityDay)
class AvailabilityDayAdmin(admin.ModelAdmin):
    ...


@register(AvailabilityTime)
class AvailabilityTimeAdmin(admin.ModelAdmin):
    ...
