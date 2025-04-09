from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def index(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProductForm()
    
    products = Product.objects.all()
    return render(request, "index.html", {"form": form, "products": products})