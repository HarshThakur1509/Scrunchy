from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Product, Cart, CartItem
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


def loginPage(request):
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

    return render(request, "app/login.html")


def logoutUser(request):
    logout(request)
    return redirect("home")


def home(request):
    products = Product.objects.all()

    context = {"products": products}
    return render(request, "app/home.html", context)


@login_required(login_url="login")
def cart(request):
    items = CartItem.objects.filter(cart__user=request.user)
    total = 0
    for item in items:
        total = total + item.product.price * item.quantity
    context = {"items": items, "total": total}
    return render(request, "app/cart.html", context)


@login_required(login_url="login")
def cart_add(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)

        cart, na = Cart.objects.get_or_create(user=request.user)
        cartitem, na = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity = cartitem.quantity + 1
        cartitem.save()

    return redirect("home")


def cart_delete(request, id):
    cart = CartItem.objects.get(id=id)
    cart.delete()
    if not CartItem.objects.filter(user=request.user).exists():
        Cart.objects.filter(user=request.user).delete()

    return redirect("cart")


def cart_plus(request, id):
    cart = CartItem.objects.get(id=id)
    cart.quantity = cart.quantity + 1
    cart.save()
    return redirect("cart")


def cart_minus(request, id):
    cart = CartItem.objects.get(id=id)
    if cart.quantity == 0:
        pass
    else:
        cart.quantity = cart.quantity - 1
    cart.save()
    return redirect("cart")
