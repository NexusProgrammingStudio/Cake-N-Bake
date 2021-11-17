"""Cake_n_Bake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'Cataloge'

urlpatterns = [
    path('Cake/', views.Product_Index_Cakes, name='Product_Index_Cakes'),
    path('Birthday/', views.Product_Index_Birthday, name='Product_Index_Birthday'),
    path('Weddings/', views.Product_Index_Weddings, name='Product_Index_Weddings'),
    path('Anniversary/', views.Product_Index_Anniversary, name='Product_Index_Anniversary'),
    path('Parents/', views.Product_Index_Parents, name='Product_Index_Parents'),
    path('Kids/', views.Product_Index_Kids, name='Product_Index_Kids'),
    path('Boyfriend/', views.Product_Index_Boyfriend, name='Product_Index_Boyfriend'),
    path('Girlfriend/', views.Product_Index_Girlfriend, name='Product_Index_Girlfriend'),
    path('Siblings/', views.Product_Index_Siblings, name='Product_Index_Siblings'),
    path('Chocolate/', views.Product_Index_Chocolates, name='Product_Index_Chocolates'),
    path('Gifts/', views.Product_Index_Gifts, name='Product_Index_Gifts'),
    path('Product/<str:Product_id>', views.View_Product, name='View_Product'),
    path('Product_Cake/<str:Product_id>', views.View_Cake, name='View_Cake'),
    path('Sleepy/<str:Product_id>', views.Sleepy, name='Sleepy'),
    path('Product_Wishlist/<str:Product_id>', views.View_Product_Wishlist, name='View_Product_Wishlist'),
    path('Cake_Wishlist/<int:Product_id>/', views.View_Cake_Wishlist, name='View_Cake_Wishlist'),
]
