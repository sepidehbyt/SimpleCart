from django.contrib.auth.models import User
from pytz import unicode

from .models import Product, Address, Cart, Order
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# token = Token.objects.create(user=...)
# print(token.key)

from .Serializers import ProductSerializer, AccountSerializer, AddressSerializer, CartSerializer, OrderSerializer,\
    AuditSerializer, UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = AccountSerializer
    permission_classes = ()

    def post_save(self, obj, created=False):
        if created:
            cart = Cart(user=obj)
            cart.save()

    def get_queryset(self,):
        user = self.request.user
        return User.objects.filter(username=user.username)


class AddressViewSet(viewsets.ModelViewSet):
    model = Address
    serializer_class = AddressSerializer

    def get_queryset(self,):
        user = self.request.user
        return Address.objects.filter(user=user)

    def pre_save(self, obj):
        obj.user = self.request.user


class CartViewSet(viewsets.ModelViewSet):
    # model = Cart
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    #
    # def get_queryset(self,):
    #     return Cart.objects.filter(user=self.request.user)

    # @action()
    # def add(self, request, pk):
    #     '''
    #         create product and add it to the cart represented by pk
    #     '''
    #     return Response({"success": True})

    # def pre_save(self, obj):
    #     obj.user = self.request.user


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self,):
    #     return Order.objects.filter(user=self.request.user)
    #
    # def pre_save(self, obj):
    #     obj.user = self.request.user
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class DetailedAccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuditSerializer
    permission_classes = (IsAdminUser,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }
    return Response(content)

