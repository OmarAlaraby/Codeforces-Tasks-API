from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from .models import Trainee

class IsRegistered(permissions.BasePermission):
    def has_permission(self, request, view):
        return Trainee.objects.first() != None

class UnRegistered(permissions.BasePermission):
    message = 'the user is already registered'
    def has_permission(self, request, view):
        if Trainee.objects.first() == None:
            return True
        else:
            raise PermissionDenied(self.message)
