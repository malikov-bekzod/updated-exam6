from django.db import models
from users.models import User


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=90)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(60)
    product_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return self.name


class QuantityRole(models.TextChoices):
    KILO = ("kg", "kilogram")
    LITER = ("l", "liter")
    PIECE = ("p", "piece")


class Product(models.Model):

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    name = models.CharField(max_length=90)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="shop/product_image/")
    old_price = models.FloatField(null=True)
    new_price = models.FloatField()
    quantity = models.CharField(
        max_length=40, choices=QuantityRole.choices, default=QuantityRole.KILO
    )
    rating = models.FloatField()
    origin_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.description[:10]


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return self.user.first_name


class Product_category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return self.product.name +" "+ self.category.name
