from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import *
from .forms import Register, ProfileForm
from .tokens import *

# Create your views here.#
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def Homepage(request):
    return render(request, 'First.html')


def About(request):
    return render(request, 'About.html')


def Signup(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            # User.objects.create_user(first_name=first_name,last_name=last_name,
            #                    email=email,username=username, password=password
            #                    )
            current_site = get_current_site(request)
            subject = 'Activate Your Cake_n_Bake Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('/account_activation_sent')
        form = Register()
        messages.add_message(request, messages.INFO, 'Invalid Sign Up! Please Try Again')
    return render(request, 'Register_Error.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/New_Login')
    else:
        return render(request, 'account_activation_invalid.html')


def Here(request):
    messages.add_message(request, messages.INFO, 'Login Here!')
    return render(request, 'Other_Login.html')


def New_Login(request):
    messages.add_message(request, messages.INFO, 'Welcome To Cake_n_Bake')
    return render(request, 'New_L.html')


def Home(request):
    return render(request, 'First.html')


def User_profile(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Login!')
        return render(request, 'Error.html')
    else:
        user = request.user
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                user.profile.First_Name = form.cleaned_data.get('first_name')
                user.profile.Last_Name = form.cleaned_data.get('last_name')
                user.profile.Phone = form.cleaned_data.get('Phone')
                user.email = form.cleaned_data.get('email')
                user.profile.pic = form.cleaned_data.get('pic')
                user.save()
                return redirect('/Home')
        else:
            form = ProfileForm(instance=user, initial={'Phone': user.profile.Phone})
            return render(request, 'Profile.html', {'form': form})


def Password(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Login!')
        return render(request, 'Error.html')
    else:
        user = request.user
        if request.method == "POST":
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/Home')
        else:

            form = PasswordChangeForm(user=request.user)
        return render(request, 'Cpass.html', {'form': form})
