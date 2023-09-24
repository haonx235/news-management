from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    """
    Override Django REST Framework IsAuthenticated permission
    """

    def has_permission(self, request, view):
        return bool(request.user)
