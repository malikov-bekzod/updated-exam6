from django.shortcuts import render
from django.views import View
from shop.models import Product,Category,Cart
from reviews.models import Testimonial
# Create your views here.

class HomePageView(View):
    def get(self,request):
        # search = request.GET.get("search") or ''
    
        products = Product.objects.all()
        bestsellers = Product.objects.filter(rating__gt=4)
        categories = Category.objects.all()
        testimonials = Testimonial.objects.all()
        context = {
            "products": products,
            "categories": categories,
            "bestsellers": bestsellers,
            "testimonials": testimonials,
        }
        return render(request, "home/home.html",context)


class ContactPageView(View):
    def get(self,request):
        return render(request,"contact.html")


class TestimonialPageView(View):
    def get(self,request):
        testimonials = Testimonial.objects.all()
        context = {
            "testimonials": testimonials,
        }
        return render(request, "testimonial.html",context)

class NotFoundView(View):
    def get(self,request):
        return render(request, "404.html")
    



class CheckoutView(View):
    def get(self,request):
        user = request.user
        carts = Cart.objects.filter(user = user)
        context = {"carts":carts}
        return render(request, "checkout.html",context)