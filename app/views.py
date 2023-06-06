from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from .models import Product, Cart

# Create your views here.


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Email or password does not exist")

    context = {"page": page}

    return render(request, "app/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def registerPage(request):
    form = UserChangeForm()
    if request.method == "POST":
        form = UserChangeForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occured")
    return render(request, "app/login.html", {"form": form})


def home(request):
    products = Product.objects.all()

    context = {"products": products}
    return render(request, "app/home.html", context)


def cart(request):
    items = Cart.objects.all()
    context = {"items": items}
    return render(request, "app/cart.html", context)


def cart_add(request, id):
    product = Product.objects.get(id=id)
    if Cart.objects.filter(name=product).exists():
        cart = Cart.objects.filter(name=product)
        for ob in cart:
            ob.quantity = ob.quantity + 1
            ob.save()
    else:
        cart = Cart.objects.create(name=product, quantity=1)
        cart.save()
    return redirect("home")


def cart_delete(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect("cart")


def cart_plus(request, id):
    cart = Cart.objects.get(id=id)
    cart.quantity = cart.quantity + 1
    cart.save()
    return redirect("cart")


def cart_minus(request, id):
    cart = Cart.objects.get(id=id)
    if cart.quantity == 0:
        pass
    else:
        cart.quantity = cart.quantity - 1
    cart.save()
    return redirect("cart")
