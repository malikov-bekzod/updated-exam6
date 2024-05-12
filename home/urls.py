from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("contact/", views.ContactPageView.as_view(), name="contact"),
    path("testimonials/", views.TestimonialPageView.as_view(), name="testimonial"),
    path("404/", views.NotFoundView.as_view(), name="404"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
]
