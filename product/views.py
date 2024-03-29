from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.contrib import messages


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "product": products,
    }
    return render(request, "product/index.html", context)


def post_product(request):
    # to insert products
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Product Added Successfully !"
            )
            return redirect("/products/addproduct/")
        else:
            messages.add_message(
                request, messages.ERROR, "Failed to add Product ! Please Verify "
            )
            return render(request, "/product/addproduct.html", {"forms": form})
        # to show add product form
    context = {
        "forms": ProductForm,
    }
    return render(request, "product/addproduct.html", context)


def post_category(request):
    # to insert products
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Category Added Successfully !"
            )
            return redirect("/products/addCategory/")
        else:
            messages.add_message(
                request, messages.ERROR, "Failed to add Category ! Please Verify "
            )
            return render(request, "/product/addCategory.html", {"forms": form})
        # to show add product form
    context = {
        "forms": CategoryForm,
    }
    return render(request, "product/addCategory.html", context)


def show_category(request):
    category = Category.objects.all()
    context = {"category": category}

    return render(request, "product/showcategory.html", context)


# todelete category


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, "Category Deleted")
    return redirect("/products/showcategory")


def delete_post(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request, messages.SUCCESS, "Product Deleted !")
    return redirect("/products/")


# to edit category
def update_category(request, category_id):
    instance1 = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Category Updated Successfully !"
            )
            return redirect("/products/showcategory/")
        else:
            messages.add_message(
                request, messages.ERROR, "Failed to Update  Category ! Please Verify "
            )
            return render(request, "/product/updatecategory.html", {"forms": form})

    context = {"forms": CategoryForm(instance=instance1)}
    return render(request, "product/updatecategory.html", context)


def update_post(request, product_id):
    instance = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Product Updated  Successfully !"
            )
            return redirect("/products/")
        else:
            messages.add_message(
                request, messages.ERROR, "Failed to Update Product ! Please Verify "
            )
            return render(request, "product/updateproduct.html", {"forms": form})
    context = {"forms": ProductForm(instance=instance)}
    return render(request, "product/updateproduct.html", context)
