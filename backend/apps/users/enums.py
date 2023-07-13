from django.db import models


class UserType(models.TextChoices):
    doctor = "D", "Doctor"
    secretary = "S", "Secretary"
    patience = "P", "Patience"
        