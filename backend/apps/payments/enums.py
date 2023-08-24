from django.db import models


class Currencies(models.TextChoices):
    IRR = "IRR", "ریال ایران"
    IRT = "IRT", "تومان ایران"

    @staticmethod
    def rial_to_toman(amount: str | int):
        assert isinstance(amount, int) or amount.isnumeric()
        if not isinstance(amount, int):
            amount = int(amount)
        return int(amount / 10)

    @staticmethod
    def toman_to_rial(amount: str | int):
        assert isinstance(amount, int) or amount.is_numeric()
        if not isinstance(amount, int):
            amount = int(amount)
        return int(amount * 10)


class PaymentStatus(models.TextChoices):
    Complete = "Complete", "complete"
    Error = "Error", "error"
    Pending = "Pending", "pending"
    Canceled = "Canceled", "canceled"
    Not_Started = "Not Started", "not_started"
