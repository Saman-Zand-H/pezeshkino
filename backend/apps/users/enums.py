from django.db import models


class UserType(models.TextChoices):
    doctor = "D", "Doctor"
    secretary = "S", "Secretary"
    patience = "P", "Patience"


class UserGender(models.TextChoices):
    male = "male", "مرد"
    female = "female", "زن"
    just_stupid = "justStupid", "ترجیح میدهم نگویم"
