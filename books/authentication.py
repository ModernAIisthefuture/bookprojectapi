
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import APIClient


class APIKeyAuthentication(BaseAuthentication):

    def authenticate(self, request):

        # Read API Key from request header
        api_key = request.headers.get("X-API-KEY")

        # If API Key is not provided,
        # allow JWT authentication to try.
        if not api_key:
            return None

        # Find client using API Key
        try:
            client = APIClient.objects.get(
                api_key=api_key,
                is_active=True
            )

        except APIClient.DoesNotExist:
            raise AuthenticationFailed(
                "Invalid or inactive API Key"
            )

        # Return authenticated client
        return (client, api_key)

    def authenticate_header(self, request):
        return "X-API-KEY"
