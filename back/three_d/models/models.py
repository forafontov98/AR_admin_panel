from django.db import models


class File(models.Model):
    file = models.FileField()


class Object(models.Model):
    file = models.ForeignKey(to=File, related_name='+', on_delete=models.CASCADE)
    preview = models.ForeignKey(to=File, related_name='+', on_delete=models.CASCADE)
    textures = models.ManyToManyField(to=File, related_name='+')


class Texture(models.Model):
    file = models.ForeignKey(to=File, related_name='+', on_delete=models.CASCADE)
