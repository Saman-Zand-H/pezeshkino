from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .viewsets.locations import OstanViewset, ShahrViewset
from .viewsets.doctors import (DoctorViewset,
                               DoctorOfficeViewset,
                               AvailabilityTimeViewset,
                               AvailabilityDayViewset)
from .viewsets.appointments import AppointmentsViewset


router = DefaultRouter()
router.register(
    prefix="city",
    viewset=ShahrViewset,
    basename="cities"
)
router.register(
    prefix="province",
    viewset=OstanViewset,
    basename="provinces"
)
router.register(
    prefix="doctor",
    viewset=DoctorViewset,
    basename="doctors"
)
router.register(
    prefix="doctor_office",
    viewset=DoctorOfficeViewset,
    basename="doctor_offices"
)
router.register(
    prefix="appointment",
    viewset=AppointmentsViewset,
    basename="appointments"
)
router.register(
    prefix="availability/day",
    viewset=AvailabilityDayViewset,
    basename="availibillity_days"
)
router.register(
    prefix="availability/time",
    viewset=AvailabilityTimeViewset,
    basename="availibillity_times"
)


urlpatterns = [
    path(route="specialties/",
         view=views.ListSpecialtiesView.as_view(),
         name="specialties"),
    path(route="get_free_times/earliest",
         view=views.GetEarliestFreeTimeView.as_view(),
         name="get_earliest_appointment"),
    path(route="get_free_times/",
         view=views.GetFreeTimesView.as_view(),
         name="get_free_times"),
    path(route="make_appointment/",
         view=views.MakeAppointmentView.as_view(),
         name="make_appointment"),
    path(route="patient/get_appointments/",
         view=views.PatientAppointmentsView.as_view(),
         name="patient_appointments")
] + router.urls
