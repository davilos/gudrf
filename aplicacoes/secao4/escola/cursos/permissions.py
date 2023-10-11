from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == "DELETE" and request.user.is_superuser:
            return True
        return False

