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
    
    class Meta:
        model = Appointment
        fields = ["office", "uuid", "office_id", "time", "datetime"]

    def create(self, validated_data):
        validated_data["office"] = validated_data.get("office_id")
        return super().create(validated_data)
