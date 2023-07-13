from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

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
        route="api/",
        view=include("api.urls")
    )
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
