from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import loginForm


# Create your views here.


def index(request):
    product = Product.objects.all().order_by("-id")[:8]
    context = {
        "product": product,
    }
    return render(request, "users/index.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "users/productdetails.html", context)


def allproducts(request):
    products = Product.objects.all()
    contextt = {"product": products}
    return render(request, "users/products.html", contextt)


# to register user
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Account Created !")
            return redirect("/register")
        else:
            messages.add_message(
                request, messages.ERROR, "Please Verify Input Fields !"
            )
            return render(request, "users/register.html", {"forms": form})

    context = {"forms": UserCreationForm}
    return render(request, "users/register.html", context)


# login
def user_login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect("/admin/dashboard")
                else:
                    return redirect("/")
            else:
                messages.add_message(
                    request, messages.ERROR, "Please Provide Real Data !"
                )
                return render(request, "users/login.html", {"forms": form})

    context = {"forms": loginForm}
    return render(request, "users/login.html", context)


def logout_user(request):
    logout(request)
    return redirect("/login")
