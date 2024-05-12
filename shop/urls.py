from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShopPageView.as_view(), name="shop"),
    path("<int:id>/", views.ShopDetailView.as_view(), name="shop_detail"),
    path("cart/<int:id>", views.CartView.as_view(), name="cart"),
    path("cart-add/<int:product_id>/<int:user_id>/", views.AddToCartView.as_view(), name="add-to-cart"),
]
