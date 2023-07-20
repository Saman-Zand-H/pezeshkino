from rest_framework import serializers
from django.db.models.aggregates import Max, Min
from iranian_cities.models import City
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from rest_framework.serializers import ModelSerializer

from .locations import ShahrSerializer
from .users import CustomUserDetailsSerializer
from api.utils import get_earliest_available_appointment
from doctors.models import (
    Doctor,
    DoctorOffice,
    AvailabilityDay,
    AvailabilityTime,
    Review
)


class AvailabilityTimeSerializer(ModelSerializer):
    day = serializers.PrimaryKeyRelatedField(write_only=True,
                                             queryset=AvailabilityDay.objects.all(),
                                             required=True)
    time = serializers.SerializerMethodField()
    
    class Meta:
        model = AvailabilityTime
        fields = ["day", "time"]
        
    def get_time(self, obj):
        return f"{obj.time:%H:%M}"


class AvailabilityDaySerializer(ModelSerializer):
    office = serializers.PrimaryKeyRelatedField(write_only=True,
                                                queryset=AvailabilityDay.objects.all(),
                                                required=True)
    times = serializers.SerializerMethodField(read_only=True)
    since = serializers.SerializerMethodField()
    till = serializers.SerializerMethodField()
    
    class Meta:
        model = AvailabilityDay
        fields = ["day_of_week", "since", "till", "get_day_of_week_display", "times", "office"]
    
    def get_times(self, obj):
        times = obj.availability_time.all()
        return AvailabilityTimeSerializer(times, many=True).data
    
    def get_since(self, obj):
        max_time = obj.availability_time.aggregate(max_time=Max("time"))["max_time"]
        return f"{max_time:%H:%M}"
    
    def get_till(self, obj):
        min_time = obj.availability_time.aggregate(min_time=Min("time"))["min_time"]
        return f"{min_time:%H:%M}"
    

class DoctorOfficeSerializer(ModelSerializer):
    availability_days = serializers.SerializerMethodField(read_only=True)
    phonenumber = serializers.SerializerMethodField()
    city = ShahrSerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=City.objects.all()
    )
    location = serializers.SerializerMethodField()
    doctor = serializers.StringRelatedField()
    doctor_specialty = serializers.SerializerMethodField()
    earliest_appointment = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DoctorOffice
        fields = [
            "id",
            "city",
            "city_id",
            "availability_days",
            "address",
            "location",
            "earliest_appointment",
            "office_title",
            "phonenumber",
            "doctor",
            "doctor_specialty",
            "created_at",
        ]
    
    def create(self, validated_data):
        validated_data["doctor"] = validated_data.get("doctor_id")
        validated_data["city"] = validated_data.get("city_id")
        location = validated_data.get("location", {"x": 0, "y": 0, "srid": 4326})
        pnt = Point(location.get("x"),
                    location.get("y"),
                    srid=location.get("srid"))
        validated_data["location"] = pnt
        return super().create(validated_data)
    
    def get_phonenumber(self, obj):
        return "-".join(obj.phonenumber.as_national.split(" ")[::-1])
    
    def get_doctor_specialty(self, obj):
        return obj.doctor.get_specialty_display()
    
    def get_availability_days(self, obj):
        availability_days = obj.office_availability.all()
        return AvailabilityDaySerializer(availability_days, many=True).data
            
    def get_location(self, obj):
        return {
            "x": obj.location.x,
            "y": obj.location.y,
            "srid": obj.location.srid
        }
        
    def get_earliest_appointment(self, obj):
        earliest = get_earliest_available_appointment(obj.id)
        return {
            "date": earliest["date"], 
            "time": earliest["obj"].time, 
            "get_day_of_week_display": earliest["obj"].day.get_day_of_week_display()
        } if bool(earliest) else {}


class OfficeIdSerializer(serializers.Serializer):
    office_id = serializers.IntegerField()
    
    def validate(self, attrs):
        if not attrs.get("office_id"):
            raise serializers.ValidationError("office_id cannot be empty.")
        office_id = attrs.get("office_id")
        if not DoctorOffice.objects.filter(id=office_id).exists():
            raise serializers.ValidationError("office instance doesn't exist.")
        return super().validate(attrs)


class MakeAppointmentSerializer(serializers.Serializer):
    datetime = serializers.DateTimeField()
    office_id = serializers.IntegerField()
    
    def validate(self, attrs):
        if not attrs.get("office_id"):
            raise serializers.ValidationError("office_id cannot be empty.")
        office_id = attrs.get("office_id")
        if not DoctorOffice.objects.filter(id=office_id).exists():
            raise serializers.ValidationError("office instance doesn't exist.")
        return super().validate(attrs)


class ReviewSerializer(serializers.ModelSerializer):
    doctor_user = serializers.SerializerMethodField(read_only=True)
    by_user = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Review
        fields = ["doctor", 
                  "doctor_user",
                  "by_user",
                  "illness",
                  "treatment_result",
                  "suggests_doctor",
                  "behavior_score",
                  "elaboration_score",
                  "skills_score",
                  "review",
                  "updated_at"]
        
    def get_doctor_user(self, obj):
        return {
            "first_name": obj.doctor.user.first_name,
            "last_name": obj.doctor.user.last_name
        }
        
    def get_by_user(self, obj):
        return {
            "first_name": obj.by_user.first_name,
            "last_name": obj.by_user.last_name,
        }
        
    def get_for_user(self, obj):
        return {
            "first_name": obj.for_user.first_name,
            "last_name": obj.for_user.last_name,
        }
        
class DoctorSerializer(ModelSerializer):
    offices = serializers.SerializerMethodField(read_only=True)
    user = CustomUserDetailsSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=get_user_model().objects.all()
    )
    rating = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Doctor
        fields = [
            "specialty", 
            "id",
            "offices",
            "get_specialty_display", 
            "upin", 
            "reviews",
            "user_id", 
            "user", 
            "rating",
            "bio",
            "verified", 
            "created_at"
        ]

    def create(self, validated_data):
        validated_data["user"] = validated_data.get("user_id")
        return super().create(validated_data)
    
    def get_reviews(self, obj):
        return ReviewSerializer(obj.doctor_reviews.all(), many=True).data
    
    def get_rating(self, obj):
        return obj.rating
    
    def get_offices(self, obj):
        return DoctorOfficeSerializer(
            instance=obj.doctor_offices.all(), many=True).data
