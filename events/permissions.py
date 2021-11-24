from rest_framework import permissions

from events.models import Application


class IsValidApplication(permissions.BasePermission):
    message = "Invalid or missing API token."

    def has_permission(self, request, view):
        return Application.objects.filter(token=request.META.get('HTTP_AUTHORIZATION')).exists()
