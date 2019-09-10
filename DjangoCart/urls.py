"""DjangoCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from Cart.views import DetailedAccountViewSet, AccountViewSet, CartViewSet, AddressViewSet, ProductViewSet, \
    OrderViewSet, UserList, UserDetail, UserViewSet

router = routers.DefaultRouter()
router.register(r'audit', DetailedAccountViewSet)
router.register(r'account', AccountViewSet, basename='account')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'addresses', AddressViewSet, basename='addresses')
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    # url(r'^api-token-auth/', views.obtain_auth_token)
    # url(r'^api-token-auth/', include('rest_framework.authtoken.views.obtain_auth_token')),
]
