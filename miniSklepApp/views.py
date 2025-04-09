from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404



def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index") 
    return render(request, "login.html")

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index") 
    else:
        form = ProductForm()
    
    return render(request, "add_product.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('index')
