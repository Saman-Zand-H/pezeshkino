from datetime import datetime, timedelta
from django.db.models import Sum, Q, F

from appointments.models import Appointment


def get_revenue_for_day(doctor_id, timestamp: datetime) -> int:
    appointments = Appointment.objects.filter(
        Q(office__doctor__id=doctor_id)
        & Q(created_at__date=timestamp.date())
    )
    return appointments.aggregate(
        total_payment=Sum(F("office__consultation_fee"))
    )["total_payment"] or 0


def get_revenues_for_last_week(doctor_id, timestamp: datetime):
    payments = []
    for i in range(7):
        payments.append(
            {
                "income": get_revenue_for_day(doctor_id, timestamp-timedelta(days=i)),
                "datetime": timestamp-timedelta(days=i)
            }
        )
    return payments


def get_total_number_of_patients(doctor_id):
    # apparently only in postgresql we can query distinct by field name.
    return (
        Appointment
        .objects
        .filter(office__doctor__id=doctor_id)
        .distinct("patient")
        .count()
    )


def get_number_of_appointments_for_day(doctor_id, timestamp: datetime):
    return (
        Appointment
        .objects
        .filter(
            Q(office__doctor__id=doctor_id)
            & Q(datetime__date=timestamp.date())
        )
        .count()
    )
