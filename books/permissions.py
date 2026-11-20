
from rest_framework.permissions import BasePermission

from .authentication import APIKeyAuthentication


class IsAuthenticatedOrAPIClient(BasePermission):

    def has_permission(self, request, view):

        # Check API Key authentication
        if isinstance(
            request.successful_authenticator,
            APIKeyAuthentication
        ):
            return True

        # Check JWT authentication
        if (
            request.user
            and request.user.is_authenticated
        ):
            return True

        return False
