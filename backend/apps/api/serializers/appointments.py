from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from doctors.models import DoctorOffice
from appointments.models import Appointment
from .doctors import DoctorOfficeSerializer


class AppointmentSerializer(ModelSerializer):
    office = DoctorOfficeSerializer(read_only=True)
    office_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                   queryset=DoctorOffice.objects.all(),
                                                   required=True)
    patient = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Appointment
        fields = ["office", "patient", "uuid", "office_id", "time", "datetime"]

    def get_patient(self, obj):
        # todo: add phone number when it was added to the user model.
        return {
            "first_name": obj.patient.first_name,
            "last_name": obj.patient.last_name
        }
