from rest_framework import permissions

from api.models import Role


class AdminPermission(permissions.BasePermission):
    edit_methods = ('POST', 'PUT', 'GET', 'DELETE')

    def has_permission(self, request, view):
        if Role.objects.filter(user_id=request.user.id).exists() and request.method in self.edit_methods:
            if Role.objects.get(user_id=request.user.id).role == 1:
                return True


class EmployeePermission(permissions.BasePermission):
    edit_methods = ('POST', 'PUT', 'GET')

    def has_permission(self, request, view):
        if Role.objects.filter(user_id=request.user.id).exists() and request.method in self.edit_methods:
            if Role.objects.get(user_id=request.user.id).role == 2:
                return True


class GuestPermission(permissions.BasePermission):
    edit_methods = ('GET',)

    def has_permission(self, request, view):
        if Role.objects.filter(user_id=request.user.id).exists() and request.method in self.edit_methods:
            if Role.objects.get(user_id=request.user.id).role == 3:
                return True
