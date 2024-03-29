from django.urls import path
from .views import *  # use * to import all


urlpatterns = [
    path("", index),
    path("productdetails/<int:product_id>", product_details),
    path("allproducts/", allproducts),
    path("register/", register_user),
    path("login/", user_login),
    path("logout/", logout_user),
]
