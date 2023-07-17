from rest_framework import serializers
from django.contrib.auth import get_user_model
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
                "city": ShahrSerializer(self.user.city).data,
                "picture": request.build_absolute_uri(self.user.picture.url) or None,
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
        data = super().validate(attrs)
        if (city_id:=data.get("city_id")) and City.objects.filter(id=city_id).exists():
            data["city"] = City.objects.get(id=city_id)
            return data
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
        return super().get_cleaned_data() | {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "picture": self.validated_data.get("picture", ""),
            "user_type": self.validated_data.get("user_type", ""),
            "city": self.validated_data.get("city", ""),
            "gender": self.validated_data.get("gender", "")
        }
    
    def custom_signup(self, request, user):
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.picture = self.cleaned_data["picture"]
        user.user_type = self.cleaned_data["user_type"]
        user.gender = self.cleaned_data["gender"]
        user.city = self.cleaned_data["city"]
        return user
