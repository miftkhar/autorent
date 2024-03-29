from rest_framework import generics

from . import models
from . import serializers


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomRegisterSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserDetailsSerializer
