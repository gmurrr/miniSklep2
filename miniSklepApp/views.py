from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

def index(request):
    # Pobieramy wszystkie produkty do wyświetlenia
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

# Widok do logowania
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")  # Po zalogowaniu wracamy na stronę główną
    return render(request, "login.html")

# Widok dla formularza dodawania produktów, dostępny tylko dla zalogowanych użytkowników
@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Po dodaniu produktu wracamy na stronę główną
    else:
        form = ProductForm()
    
    return render(request, "add_product.html", {"form": form})
