from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Product, Category, Product_category,Cart
from reviews.models import Review
from users.models import User

# Create your views here.


class ShopPageView(View):
    def get(self, request):
        search = request.GET.get("search") or ""
        products = Product.objects.filter(name__icontains=search)
        categories = Category.objects.all()
        featured_products = Product.objects.filter(old_price__isnull=False)
        context = {
            "products": products,
            "categories": categories,
            "featured_products": featured_products,
        }
        return render(request, "shop/shop.html", context)


class ShopDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        products = Product.objects.all()
        categories = Category.objects.all()
        reviews = Review.objects.all()
        featured_products = Product.objects.filter(old_price__isnull=False)
        context = {
            "product": product,
            "products": products,
            "reviews": reviews,
            "categories": categories,
            "featured_products": featured_products,
        }
        return render(request, "shop/product_detail.html", context)

class CartView(LoginRequiredMixin,View):
    def get(self,request,id):
        user = User.objects.get(id=id)
        carts = Cart.objects.filter(user=user)
        total_sum = 0
        for cart in carts:
            total_sum += cart.product.new_price
        context = {
            "carts": carts,
            "total_sum": total_sum,
        }
        return render(request, "cart/cart.html",context)


class AddToCartView(LoginRequiredMixin,View):
    def get(self,request,product_id,user_id):
        product = Product.objects.get(id=product_id)
        user = User.objects.get(id=user_id)
        cart = Cart.objects.create(
            product = product,
            user = user
        )
        cart.save()
        return redirect('cart', user.id)
