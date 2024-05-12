from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserAPIViewSet,
    ReviewApiViewSet,
    TestimonialApiViewSet,
    CountryApiViewSet,
    CategoryApiViewSet,
    ProductApiViewSet,
    CartApiViewSet,
    Product_categoryApiViewSet,
    SongsAPIViewSet,
    AlbomsAPIViewSet,
    ArtistsAPIViewSet,
)

router = DefaultRouter()
router.register(prefix="reviews", viewset=ReviewApiViewSet, basename="reviews")
router.register(prefix="products", viewset=ProductApiViewSet, basename="products")
router.register(prefix="countries", viewset=CountryApiViewSet, basename="countries")
router.register(
    prefix="testimonials", viewset=TestimonialApiViewSet, basename="testimonials"
)
router.register(prefix="categories", viewset=CategoryApiViewSet, basename="categories")
router.register(prefix="cart", viewset=CartApiViewSet, basename="cart")
router.register(prefix="songs", viewset=SongsAPIViewSet, basename="songs")
router.register(prefix="alboms", viewset=AlbomsAPIViewSet, basename="alboms")
router.register(prefix="artists", viewset=ArtistsAPIViewSet, basename="artist")
router.register(prefix="users", viewset=UserAPIViewSet, basename="users")
router.register(
    prefix="product_category",
    viewset=Product_categoryApiViewSet,
    basename="product_category",
)

urlpatterns = [
    path("", include(router.urls)),
]
