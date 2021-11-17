from django import forms
from django.contrib.auth.models import User
from .models import Wishlist, Cart, Order, Checkout

Width = "'width:500px'"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class Wish(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['Weight', 'Egg_or_Eggless']


class Cart1(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['Weight', 'Egg_or_Eggless', 'Qty']


class Cart2(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['Qty']


class Forders(forms.ModelForm):
    class Meta:
        model = Order
        fields = []


class Check(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control', 'placeholder': 'First Name', 'style': Width}),
                                 max_length=30,
                                 required=True)
    last_name = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control', 'placeholder': 'Last Name', 'style': Width}),
                                max_length=30,
                                required=True)

    contact_no = forms.IntegerField(widget=forms.TextInput
    (attrs={'class': 'form-control', 'placeholder': 'contact', 'style': Width}), required=True)

    email = forms.CharField(widget=forms.EmailInput
    (attrs={'class': 'form-control', 'placeholder': 'Email Address', 'style': Width}),
                            max_length=50,
                            required=True)
    Address = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control', 'placeholder': 'Address', 'style': Width}), required=True)

    class Meta:
        model = Checkout
        fields = ['first_name', 'last_name', 'contact_no', 'email', 'Address']
