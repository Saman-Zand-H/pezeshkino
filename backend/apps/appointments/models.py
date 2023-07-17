from django.db import models
from django.conf import settings
from django.utils import timezone

from doctors.models import (AvailabilityTime, 
                            DoctorOffice)


class Appointment(models.Model):
    time = models.ForeignKey(AvailabilityTime,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name="availability_appointments")
    patient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name="appointments")
    # this can make it more convenient to retrieve the appointments
    office = models.ForeignKey(DoctorOffice,
                               on_delete=models.CASCADE,
                               related_name="office_appointments")
    datetime = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = [
            ["time", "datetime"]
        ]
    