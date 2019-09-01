from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .Serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('created_date')
    serializer_class = ProductSerializer
