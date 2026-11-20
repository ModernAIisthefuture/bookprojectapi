
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


class LoginView(TokenObtainPairView):

    # Login should work without an existing token
    authentication_classes = []

    permission_classes = [AllowAny]


class RefreshView(TokenRefreshView):

    # Refresh should work without an access token
    authentication_classes = []

    permission_classes = [AllowAny]
