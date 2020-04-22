from rest_framework import viewsets, mixins, generics
from rest_framework.parsers import MultiPartParser, FormParser

from ..models.models import Texture, Object, File
from .serializers import (
    TextureSerializer,
    ObjectSerializer,
    FileSerializer,
    ObjectRetreiveSerializer,
    TextureRetrieveSerializer,
)


class TexturesAdminViewset(
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = TextureSerializer
    queryset = Texture.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in {"POST", "PUT", "PATCH"} or "pk" in self.kwargs:
            return TextureSerializer

        return TextureRetrieveSerializer


class ObjectsAdminViewset(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in {"POST", "PUT", "PATCH"}:
            return ObjectSerializer

        return ObjectRetreiveSerializer


class FileViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    parser_classes = [MultiPartParser, FormParser]
