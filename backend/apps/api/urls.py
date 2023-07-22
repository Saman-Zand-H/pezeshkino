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
    path(route="initiate_appointment/",
         view=views.InitiateAppointmentView.as_view(),
         name="initiate_appointment"),
    path(route="patient/get_appointments/",
         view=views.PatientAppointmentsView.as_view(),
         name="patient_appointments"),
    path(route="transaction/validate/",
         view=views.ValidateTransactionView.as_view(),
         name="validate_transaction"),
    path(route="transaction/for/",
         view=views.ListForTransactionsView.as_view(),
         name="list_for_transactions"),
    path(route="transaction/by/",
         view=views.ListByTransactionsView.as_view(),
         name="list_by_transactions"),
    path(route="review/",
         view=views.ReviewView.as_view(),
         name="review"),
    path(route="register/doctor/",
         view=views.RegisterDoctorView.as_view(),
         name="register_doctor"),
    path(route="dashboard/home/",
         view=views.DashboardHomeDataView.as_view(),
         name="home_dashboard_data")
] + router.urls
