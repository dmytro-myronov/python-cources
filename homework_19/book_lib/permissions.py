from rest_framework import permissions
from rest_framework.permissions import BasePermission
from django.http import HttpRequest, HttpResponse


class isAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to modify content, while others can only read.
    """
    def has_permission(self, request:HttpRequest, view) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff