from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey('auth.User', related_name="addresses", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    mobile = models.CharField(max_length=11, blank=True, null=True)


class Product(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    # user = models.ForeignKey('auth.User', related_name="carts", on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)


class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.CASCADE)
    # items = models.ManyToManyField(Product)
    # user = models.ForeignKey('auth.User', related_name="orders", on_delete=models.CASCADE)
