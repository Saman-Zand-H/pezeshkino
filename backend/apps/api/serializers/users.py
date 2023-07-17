from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer

from users.enums import UserType


UserModel = get_user_model()


class CustomUserDetailsSerializer(UserDetailsSerializer):
    picture = serializers.ImageField(use_url=True,
                                     allow_empty_file=True,
                                     required=False,
                                     read_only=True)
    
    class Meta:
        extra_fields = []
        extra_fields.extend(
            [UserModel.USERNAME_FIELD, 
             "first_name", 
             "last_name", 
             "name",
             "picture"])
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ["pk", "email"]


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    picture = serializers.ImageField(use_url=True, 
                                     allow_empty_file=True,
                                     required=False)
    user_type = serializers.ChoiceField(choices=UserType)
    
    def get_cleaned_data(self):
        return super().get_cleaned_data() | {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "picture": self.validated_data.get("picture", ""),
            "user_type": self.validated_data.get("user_type", "")
        }
    
    def custom_signup(self, request, user):
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.picture = self.cleaned_data["picture"]
        user.user_type = self.cleaned_data["user_type"]
        return user
