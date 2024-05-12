from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=60)
    image = models.URLField(null=True)
    last_update = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]


class Albom(models.Model):
    title = models.CharField(max_length=60)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    image = models.URLField(null=True)
    last_update = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]


class Song(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField(null=True)
    albom = models.ForeignKey(Albom, on_delete=models.SET_NULL, null=True)
    last_update = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]
