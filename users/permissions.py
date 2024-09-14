from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to users with an admin role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsSuperAdmin(BasePermission):
    """
    Allows access only to users with a superAdmin role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'superAdmin'
