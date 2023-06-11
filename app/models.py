from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True
    )
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.cart) + " -> " + str(self.product)
