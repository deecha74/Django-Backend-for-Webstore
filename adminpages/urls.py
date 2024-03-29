from django.urls import path
from .views import *

# use * to import all


urlpatterns = [path("dashboard/", admin_home)]
