from rest_framework import serializers

from ..models.models import Object, Texture, File


class ObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Object
        fields = (
            'id',
            'file',
            'preview',
            'textures',
        )


class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = File
        fields = (
            'id',
            'file',
        )


class ObjectRetreiveSerializer(serializers.ModelSerializer):
    file = FileSerializer()
    textures = FileSerializer(many=True)
    preview = FileSerializer()

    class Meta:
        model = Object
        fields = (
            'id',
            'file',
            'textures',
            'preview',
        )


class TextureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Texture
        fields = (
            'id',
            'file',
        )


class TextureRetrieveSerializer(serializers.ModelSerializer):
    file = FileSerializer()

    class Meta:
        model = Texture
        fields = (
            'id',
            'file',
        )


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'id',
            'file',
        )
