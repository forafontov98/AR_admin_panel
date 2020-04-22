from rest_framework import serializers
from .models import Texture, Object, File


class FileSerializer(serializers.Serializer):
    name = serializers.CharField(source='file', read_only=True)
    file = serializers.FileField()

    class Meta:
        model = File
        fields = (
            'name',
            'file',
        )



class TextureSerialzier(serializers.Serializer):
    file = FileSerializer(read_only=True)

    class Meta:
        model = Texture
        fields = (
            'id',
            'file',
        )


class ObjectSerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True)
    textures = FileSerializer(many=True, read_only=True)
    preview = serializers.FileField(source='file.file')

    class Meta:
        model = Object
        fields = (
            'id',
            'file',
            'textures',
            'preview',
        )
