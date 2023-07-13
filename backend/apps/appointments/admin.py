from django.contrib.admin import ModelAdmin
from django.contrib.admin.decorators import register

from .models import Appointment


@register(Appointment)
class AppointmentAdmin(ModelAdmin):
    ...
