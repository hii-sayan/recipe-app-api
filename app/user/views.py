"""
Views for the user API
"""
from rest_framework import generics, authentication, permissions
from user.serializers import UserSerializers, AuthTokenSerializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class CreateUserView(generics.CreateAPIView):
    """Create a new user in  the system."""
    serializer_class = UserSerializers


class CreateTokenView(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class = AuthTokenSerializers
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializers
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrive nad retunr the authenticated user"""
        return self.request.user