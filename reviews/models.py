from django.db import models
from shop.models import Product
from users.models import User
from mdeditor.fields import MDTextField


# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = MDTextField(null=True, blank=True)
    rate = models.FloatField(null=True)
    readed = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]


class Testimonial(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="testimonials/")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    readed = models.PositiveIntegerField(default=0)
    profession = models.CharField(max_length=60)

    # created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]
