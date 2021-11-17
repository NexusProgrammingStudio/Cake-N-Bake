from django import forms
from .models import Product, Cart_Cateloge, Wishlist_Cateloge


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Price_500gms', 'Price_1kg', 'Price_2kg', 'Price_Other_Products', 'Pic', 'desc']


class Cart1(forms.ModelForm):
    class Meta:
        model = Cart_Cateloge
        fields = ['Weight', 'Egg_or_Eggless', 'Qty']


class Cart2(forms.ModelForm):
    class Meta:
        model = Cart_Cateloge
        fields = ['Qty']


class Wish1(forms.ModelForm):
    class Meta:
        model = Wishlist_Cateloge
        fields = []


class Wish2(forms.ModelForm):
    class Meta:
        model = Cart_Cateloge
        fields = ['Weight']
