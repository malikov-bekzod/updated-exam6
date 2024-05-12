from rest_framework import serializers

from reviews.models import Review, Testimonial
from users.models import User
from shop.models import Country,Category,Product,Cart,Product_category
from music.models import Albom, Artist, Song

# General serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name", "last_name", "is_staff", "is_active", "date_joined")

# REVIEW SERIALIZERS

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = (
            "id",
            "product",
            "user",
            "text",
            "rate",
            "readed",
            "created_date",
        )

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ("id", "text", "image", "first_name", "last_name", "profession","readed")


# SHOP SERIALIZERS

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("__all__")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")


class ProductSerializer(serializers.ModelSerializer):
    origin_country = CountrySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ("__all__")


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"


class Product_categorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Product_category
        fields = "__all__"

# MUSIC serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name", "image", "last_update", "created_date")


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Albom
        fields = ("title", "artist", "image", "last_update", "created_date")


class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ("title", "albom", "image", "last_update", "created_date")
