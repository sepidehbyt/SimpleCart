from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Address, Cart, Order


class UserSerializer(serializers.ModelSerializer):
    # carts = serializers.PrimaryKeyRelatedField(many=True, queryset=Cart.objects.all())
    # addresses = serializers.PrimaryKeyRelatedField(many=True, queryset=Address.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        # fields = ['id', 'username', 'carts', 'addresses', 'orders']
        fields = ['id', 'username', 'orders']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'addresses', 'carts')
        write_only_fields = 'password'

    def restore_object(self, attrs, instance=None):
        user = super(AccountSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('url', 'first_name', 'last_name', 'street_address', 'city', 'mobile')


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('url', 'items')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url', 'product_name', 'price')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        # owner = serializers.ReadOnlyField(source='owner.username')
        # fields = ('url', 'items', 'cart', 'owner')
        fields = ('url', 'items', 'cart',)


class AuditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'addresses', 'carts')
        write_only_fields = 'password'
    depth = 3
