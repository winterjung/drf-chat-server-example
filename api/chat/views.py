from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from api.chat import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class RoomViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class MessageViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
