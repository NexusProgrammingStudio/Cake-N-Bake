from django import forms
from django.contrib.auth.models import User


class Register(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput
    (attrs={'class': 'form-control'}), label="Confirm your password", max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super(Register, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control'}), max_length=30, required=True)

    last_name = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control'}),
                                max_length=30,
                                required=True)
    Phone = forms.IntegerField(widget=forms.TextInput
    (attrs={'class': 'form-control'}),
                               required=True)

    email = forms.CharField(widget=forms.EmailInput
    (attrs={'class': 'form-control'}),
                            max_length=30, )

    pic = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'Phone', 'email']


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form'}),
        label="Old Password",
        required=True)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form'}),
        label="New Password",
        required=True)

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form'}),
        label="Confirm your Password",
        required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_password']
