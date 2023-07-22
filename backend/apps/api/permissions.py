from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (request.user and request.user.is_superuser) 
            or request.method in SAFE_METHODS
        )


class IsDoctor(IsAuthenticated):
    def has_permission(self, request, view):
        return (
            super().has_permission(request, view) 
            and request.user.user_type == "D"
        )
