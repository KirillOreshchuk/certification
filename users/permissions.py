from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    massage = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsCurrentUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.pk == request.user.pk


class IsStaffOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True


class IsActive(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active
