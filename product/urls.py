from django.urls import path
from .views import (
    index,
    show_category,
    post_product,
    post_category,
    delete_category,
    delete_post,
    update_category,
    update_post,
)  # use * to import all


urlpatterns = [
    path("", index),
    path("addproduct/", post_product),
    path("addCategory/", post_category),
    path("showcategory/", show_category),
    path("deletecategory/<int:category_id>", delete_category),
    path("deletepost/<int:product_id>", delete_post),
    path("updatecategory/<int:category_id>", update_category),
    path("updateproduct/<int:product_id>", update_post),
]
