from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm

# Create your views here.
class LoginPageView(View):
    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            context = {"user": user}

            return render(request, "home/home.html", context)
        else:
            print("errorsss")
            context = {"form": login_form}
            return render(request, "users/login.html", context)


class RegisterPageView(View):
    def get(self, request):
        return render(request, "users/register.html")

    def post(self, request):
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "username": request.POST["username"],
            "password": password1,
        }
        user = UserRegisterForm(data, request.FILES)
        if user.is_valid() and password1 == password2:
            user.save()
            return redirect("login-page")
        else:
            print("ERRor")
            context = {"form": user}
            return render(request, "users/register.html", context)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")
