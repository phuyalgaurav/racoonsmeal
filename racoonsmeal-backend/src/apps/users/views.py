from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User, UserProfile
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    UserProfileSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Password updated successfully"}, status=status.HTTP_200_OK
        )


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile
