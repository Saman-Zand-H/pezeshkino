from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, 
                                        BaseUserManager, 
                                        PermissionsMixin)
from iranian_cities.models import City

from .enums import UserType, UserGender


class UsersManager(BaseUserManager):
    def _create_user(self,
                     username,
                     password,
                     email,
                     is_active,
                     is_staff,
                     is_superuser,
                     picture,
                     first_name,
                     last_name):
        normalized_email = None
        if bool(email):
            self.normalize_email(email)
        now = timezone.now()
        user = self.create(
            username=username,
            email=normalized_email,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            picture=picture,
            first_name=first_name,
            last_name=last_name,
            date_joined=now
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,
                    username=None,
                    password=None,
                    email=None,
                    first_name=None,
                    last_name=None,
                    picture=None,
                    is_active=True):
        return self._create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            picture=picture,
            is_active=is_active,
            is_superuser=False,
            is_staff=False
        )
    
    def create_staff(self,
                     username=None,
                     password=None,
                     email=None,
                     first_name=None,
                     last_name=None,
                     picture=None,
                     is_active=True):
        return self._create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            picture=picture,
            is_active=is_active,
            is_superuser=False,
            is_staff=True
        )
    
    def create_superuser(self,
                         username=None,
                         password=None,
                         email=None,
                         first_name=None,
                         last_name=None,
                         picture=None,
                         is_active=True):
        return self._create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            picture=picture,
            is_active=is_active,
            is_superuser=True,
            is_staff=True
        )


class UserModel(AbstractBaseUser, PermissionsMixin):    
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    gender = models.CharField(choices=UserGender.choices, max_length=10, default="justStupid")
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             related_name="city_users")
    user_type = models.CharField(max_length=1,
                                 choices=UserType.choices,
                                 default=UserType.patience)
    picture = models.ImageField(upload_to="avatars",
                                blank=True,
                                null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsersManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    class Meta:
        verbose_name_plural = "UserModel"

    @property
    def name(self):
        return (f"{'DR.' if self.user_type == 'D' else '' } "
                f"{self.first_name.title()} {self.last_name.title()}").strip()
