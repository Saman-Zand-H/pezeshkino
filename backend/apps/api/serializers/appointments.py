from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from doctors.models import DoctorOffice
from appointments.models import Appointment
from .doctors import DoctorOfficeSerializer


class AppointmentSerializer(ModelSerializer):
    doctor_office = DoctorOfficeSerializer(read_only=True)
    doctor_office_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                          queryset=DoctorOffice.objects.all(),
                                                          required=True)
    
    class Meta:
        model = Appointment
        fields = ["doctor_office", "doctor_office_id", "time", "datetime"]

    def create(self, validated_data):
        validated_data["doctor_office"] = validated_data.get("doctor_office_id")
        return super().create(validated_data)
