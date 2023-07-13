from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return bool(
            (request.user and request.user.is_superuser) 
            or request.method in SAFE_METHODS
        )
