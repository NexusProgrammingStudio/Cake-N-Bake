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

app_name = 'Services'

urlpatterns = [
    # url(r'^Orders/([\w]+)$',views.Orders, name='Order'),
    path('V_Orders/<str:d>/', views.Myorder, name='Myorder'),
    path('Invoice/', views.Invoice, name='Invoice'),
    path('Pay/', views.pay, name='Pay'),
    path('Checkout_Option/<str:d>/', views.Checkout_Option, name='Checkout'),
    path('Choice/<str:d>/', views.Choice, name='Choice'),
    path('Old/<str:d>/', views.Old, name='Old'),
    path('New/<str:d>/', views.New, name='New'),
    path('View_Order/<int:d>/', views.View_Order, name="View_Order"),
    # Cart
    path('Cart_View/<str:d>', views.Cart_View, name='Cart_View'),
    path('Delete_Cake/<int:d>/<str:u>/<str:f>', views.Delete_From_Cart, name='Delete_From_Cart'),
    path('Product/<str:Product_id>/<str:u>', views.Add_Product_To_Cart, name='Add_Product_To_Cart'),
    path('Product_Cake/<str:Product_id>/<str:u>', views.Add_Cake_To_Cart, name='Add_Cake_To_Cart'),
    # Wishlist
    path('Wishlist/<str:d>', views.Wishlist_View, name='Wishlist'),
    path('Delete_Wishlist/<int:d>/<str:u>/', views.Delete_From_Wishlist, name='Delete_From_Wishlist'),
    path('Product_Wishlist/<str:Product_id>/<str:u>', views.Add_Product_To_Wishlist, name='Add_Product_To_Wishlist'),
    path('Cake_Wishlist/<str:Product_id>/<str:u>', views.Add_Cake_To_Wishlist, name='Add_Cake_To_Wishlist'),
]
