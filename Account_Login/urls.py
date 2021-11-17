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
from django.urls import path, re_path

from . import views
from .FPass import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'Account_Login'

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('Login/Error/', LoginView.as_view(template_name='Login_Error.html'), name='Login'),
    path('Logout', LogoutView.as_view(next_page='/Home/'), name='Logout'),
    path('Password/', views.Password, name='Password'),

    path('About/', views.About, name='About'),
    path('Signup/', views.Signup, name='Signup'),

    path('Home/', views.Home, name='Home'),
    path('New_Login/', views.New_Login, name='New_Login'),
    path('Profile/', views.User_profile, name='Profile'),
    path('Login_Here/', views.Here, name='Here'),

    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),

    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate,
            name='activate'),

    path('password_reset/', PasswordResetView.as_view(template_name='password_reset_email.html'),
         name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
            name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]
