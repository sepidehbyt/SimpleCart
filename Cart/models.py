from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name="carts", on_delete=models.CASCADE)


class CartItems(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, blank=True, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=False, on_delete=models.CASCADE)


class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.CASCADE)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey('auth.User', related_name="orders", on_delete=models.CASCADE)
