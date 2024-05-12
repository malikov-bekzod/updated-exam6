from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to="users/profile_image/", null=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=["id"])
        ]