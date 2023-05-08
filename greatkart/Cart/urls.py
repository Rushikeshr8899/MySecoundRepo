"""
URL configuration for greatkart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.cart,name="cart"),
    path('add_cart/<int:product_id>', views.add_cart, name="add_cart"),
    path('remove_cart_item/<int:product_id>',views.remove_cart_item,name="remove_cart_item"),
    path('remove_cart/<int:product_id>',views.remove_cart,name="remove_cart"),
    path('cart_prod/',views.cart_prod,name="cart_prod"),
    path('contact_us/',views.contact_us,name="contact_us")
]







