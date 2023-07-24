from rest_framework import serializers
from django.contrib.auth import get_user_model
from collections import deque
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from iranian_cities.models import City

from users.enums import UserType, UserGender
from .locations import ShahrSerializer


UserModel = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        request = self.context["request"]
        data.update({
            "user": {
                "username": self.user.username,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "user_type": self.user.user_type,
                "city": ShahrSerializer(self.user.city).data,
                "picture": (request.build_absolute_uri(self.user.picture.url) 
                            if self.user.picture else None),
                "gender": self.user.gender
            }
        })
        return data


class CustomUserDetailsSerializer(UserDetailsSerializer):
    picture = serializers.ImageField(use_url=True,
                                     allow_empty_file=True,
                                     required=False)
    city = ShahrSerializer(read_only=True)
    city_id = serializers.IntegerField(write_only=True,
                                       required=False)
    
    class Meta:
        extra_fields = [
            UserModel.USERNAME_FIELD, 
            "first_name", 
            "last_name", 
            "user_type",
            'username',
            "name",
            "city",
            "city_id",
            "gender",
            "picture"
        ]
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ["pk", "email", "user_type"]
    
    def validate(self, attrs):
        if (city_id:=attrs.get("city_id")) and City.objects.filter(id=city_id).exists():
            attrs["city"] = City.objects.get(id=city_id)
            return attrs
        elif not bool(city_id):
            return attrs
        raise serializers.ValidationError("invalid city_id.", "invalid_city")
    
    def validate_username(self, username):
        if self.instance.username == username:
            return username
        return super().validate_username(username)


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    picture = serializers.ImageField(use_url=True, 
                                     allow_empty_file=True,
                                     required=False)
    user_type = serializers.ChoiceField(choices=UserType)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), required=False)
    gender = serializers.ChoiceField(choices=UserGender.choices, required=False)
    
    def get_cleaned_data(self):
        data = {
            "first_name": self.validated_data.get("first_name"),
            "last_name": self.validated_data.get("last_name"),
            "user_type": self.validated_data.get("user_type"),
        }
        optional_fields = ["city", "gender", "picture"]
        for field_name in optional_fields:
            if self.validated_data.get(field_name) is not None:
                data[field_name] = self.validated_data.get(field_name)
        return super().get_cleaned_data() | data
    
    def custom_signup(self, request, user):
        optional_fields = ["city", "gender", "picture"]
        self.cleaned_data = self.get_cleaned_data()
        for field_name in optional_fields:
            if self.cleaned_data.get(field_name) is not None:
                setattr(user, field_name, self.cleaned_data.get(field_name))
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.user_type = self.cleaned_data["user_type"]
        return user
