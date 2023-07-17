from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenRefreshView, 
                                            TokenObtainPairView,
                                            TokenVerifyView)

urlpatterns = [
    path(
        route='admin/', 
        view=admin.site.urls
    ),
    
    path(
        route="accounts/",
        view=include("allauth.urls")
    ),
    path(
        route='dj-rest-auth/', 
        view=include("dj_rest_auth.urls")
    ),
    path(
        route='dj-rest-auth/registration/', 
        view=include('dj_rest_auth.registration.urls')
    ),
    path(
        route="api/token/",
        view=TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        route="api/token/refresh/",
        view=TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path(
        route="api/token/verify/",
        view=TokenVerifyView.as_view(),
        name="token_verify"
    ),
    
    path(
        route="api/",
        view=include("api.urls")
    )
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
