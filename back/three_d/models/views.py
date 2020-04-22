from rest_framework import viewsets, mixins

from ..users.permissions import IsUserOrReadOnly
from .models import Texture, Object
from . import serializers


class TexturesListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Texture.objects.all()
    serializer_class = serializers.TextureSerialzier


class ObjectsListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Object.objects.all()
    serializer_class = serializers.ObjectSerializer
