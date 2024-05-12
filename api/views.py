from django.shortcuts import render,redirect
from django.db.transaction import atomic

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action

# Create your views here.
from .serializers import UserSerializer,ReviewSerializer,TestimonialSerializer,CountrySerializer,CategorySerializer, ProductSerializer,CartSerializer,Product_categorySerializer,AlbomSerializer,SongSerializer,ArtistSerializer

from users.models import User
from shop.models import Product,Product_category, Cart,Country,Category
from music.models import Song,Albom, Artist
from reviews.models import Review,Testimonial  

class UserAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["id",""]
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=["get"])
    def admins(self, request, *args, **kwargs):
        admins = User.objects.filter(is_staff = True)
        serializer = UserSerializer(admins, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=["get"])
    def experienced(self, request, *args, **kwargs):
        old_users = User.objects.all().order_by("date_joined")
        serializer = UserSerializer(old_users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ReviewApiViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["text"]
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=["get"])
    def newest(self, request, *args, **kwargs):
        reviews = Review.objects.all().order_by("-created_date")
        serializer = ReviewSerializer(reviews,many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False,methods=["get"])
    def rating(self,request,*args,**kwargs):
        reviews = Review.objects.all().order_by("-rate")
        serializer = ReviewSerializer(reviews, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True,methods=["get"])
    def read(self,request,*args,**kwargs):
        review = self.get_object()
        with atomic():
            review.readed+=1
            review.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def top(self, request,*args,**kwargs):
        reviews = self.get_queryset()
        reviews = reviews.order_by("-readed")
        serializer = ReviewSerializer(reviews, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class TestimonialApiViewSet(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["text","first_name"]
    pagination_class = LimitOffsetPagination

    # @action(detail=False, methods=["get"])
    # def newest(self, request, *args, **kwargs):
    #     testimonials = self.get_queryset().order_by("-created_date")
    #     serializer = TestimonialSerializer(testimonials, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True, methods=["get"])
    def read(self, request, *args, **kwargs):
        testimonial = self.get_object()
        with atomic():
            testimonial.readed += 1
            testimonial.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    @action(detail=False, methods=["get"])
    def top(self, request,*args,**kwargs):
        testimonials = self.get_queryset()
        testimonials = testimonials.order_by("-readed")
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CountryApiViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class CategoryApiViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name", "description"]
    pagination_class = LimitOffsetPagination


class CartApiViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["user__first_name"]
    pagination_class = LimitOffsetPagination


class Product_categoryApiViewSet(ModelViewSet):
    queryset = Product_category.objects.all()
    serializer_class = Product_categorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["product__name", "category__name"]
    pagination_class = LimitOffsetPagination


class SongsAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title"]
    pagination_class = LimitOffsetPagination


class AlbomsAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title"]
    pagination_class = LimitOffsetPagination


class ArtistsAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination
