from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("cart/add/<int:id>", views.cart_add, name="cart_add"),
    path("cart/delete/<int:id>", views.cart_delete, name="cart_delete"),
    path("cart/plus/<int:id>", views.cart_plus, name="cart_plus"),
    path("cart/minus/<int:id>", views.cart_minus, name="cart_minus"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
