from uuid import uuid4
from django.db import models
from django.db.models import Q
from django.conf import settings
from django.utils import timezone

from doctors.models import (AvailabilityTime, 
                            DoctorOffice)
from payments.models import MonetaryTransaction
from payments.enums import PaymentStatus


class AppointmentManager(models.Manager):
    def paid_appointments(self):
        return super().get_queryset().filter(
            Q(transaction__not=None) 
            & Q(transaction__status=PaymentStatus.Complete)
        )


class Appointment(models.Model):
    uuid = models.UUIDField(default=uuid4,
                            unique=True,
                            auto_created=True,
                            editable=False)
    transaction = models.OneToOneField(MonetaryTransaction,
                                      on_delete=models.CASCADE,
                                      related_name="appointment",
                                      blank=True,
                                      null=True)
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
    
    objects = AppointmentManager()
    
    @property
    def is_paid(self):
        return (self.transaction is not None 
                and self.transaction.is_success)
    
    class Meta:
        unique_together = [
            ["time", "datetime"]
        ]
    