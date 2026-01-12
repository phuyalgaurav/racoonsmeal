from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import User, UserProfile
from .serializers import (
    RegisterSerializer,
    UserProfileNestedSerializer,
    ChangePasswordSerializer,
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


class UserProfileView(
    generics.CreateAPIView, generics.UpdateAPIView, generics.RetrieveAPIView
):
    queryset = UserProfile.objects.select_related("user").all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileNestedSerializer
    lookup_url_kwarg = "username"

    def get_object(self):
        username = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(self.get_queryset(), user__username=username)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save() if serializer.is_valid() else None
