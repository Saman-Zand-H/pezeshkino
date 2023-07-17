from typing import List
from django.utils import timezone
from django.db.models import Q, QuerySet
from datetime import datetime, timedelta, date, time

from appointments.models import Appointment
from doctors.models import AvailabilityDay, AvailabilityTime


def get_available_times(office_id: int, date_obj: date) -> QuerySet[AvailabilityTime]:
    if not (
        AvailabilityDay
        .objects
        .filter(Q(day_of_week=date_obj.isoweekday())
                & Q(office__id=office_id))
        .exists()
    ):
        return
    taken_appointments = Appointment.objects.filter(
        Q(office__id=office_id) 
        & Q(datetime__date=date_obj)
    )
    free_times = (
        AvailabilityTime
        .objects
        .filter(Q(day__day_of_week=date_obj.isoweekday())
                & Q(day__office__id=office_id))
        .exclude(id__in=taken_appointments.values("time"))
        .order_by("time")
    )
    return free_times


def get_available_times_in_range(
        office_id, 
        timestamp=timezone.now().timestamp(), 
        date_range=7
    ) -> List[dict[datetime, QuerySet[AvailabilityTime]]]:
    base_datetime_obj = datetime.fromtimestamp(timestamp).date()
    results = []
    for i in range(date_range):
        date_delta = base_datetime_obj + timedelta(days=i)
        available_time = get_available_times(office_id, date_delta)
        if available_time and available_time.exists():
            results.append(
                {"obj": available_time,
                 "date": date_delta}
            )
    return results


def get_earliest_available_appointment(office_id):
    available_times = get_available_times_in_range(office_id)
    if not bool(available_times):
        return {}
    available_times.sort(key=lambda i: i["obj"].first().time)
    result = available_times[0]
    return {"date": result["date"], "obj": result["obj"].first()}


def check_availability(office_id, datetime_obj):
    availabe_qs = get_available_times(office_id, datetime_obj.date())
    return availabe_qs.exists() if availabe_qs else False
