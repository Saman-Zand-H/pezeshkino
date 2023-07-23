from uuid import uuid4
from django.db import models
from django.conf import settings

from .enums import Currencies, PaymentStatus


class MonetaryTransaction(models.Model):
    by_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name="by_transactions")
    for_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name="for_transactions")
    currency = models.CharField(max_length=3, 
                                choices=Currencies.choices, 
                                default=Currencies.IRR)
    amount = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid4,
                            unique=True,
                            auto_created=True,
                            editable=False)
    trackId = models.CharField(unique=True)
    status = models.CharField(choices=PaymentStatus.choices, default=PaymentStatus.Pending)
    reference_number = models.CharField(null=True, blank=True)
    response_result = models.TextField(null=True, blank=True)
    extra_information = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    payment_time = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.pk} - {self.trackId}"
    
    @property
    def is_success(self):
        return self.status == PaymentStatus.Complete
    