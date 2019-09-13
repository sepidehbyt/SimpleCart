from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Cart, Order


class UserSerializer(serializers.ModelSerializer):
    # carts = serializers.PrimaryKeyRelatedField(many=True, queryset=Cart.objects.all())
    # orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        # fields = ['id', 'username', 'password', 'email', 'carts', 'orders']
        fields = ['id', 'username', 'password', 'email']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')
        write_only_fields = 'password'

    def restore_object(self, attrs, instance=None):
        user = super(AccountSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('url', 'owner')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url', 'product_name', 'price')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('url', 'owner', 'cart', 'totalPrice')
