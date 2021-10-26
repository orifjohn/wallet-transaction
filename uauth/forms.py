from django import forms


class UserRegisterForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    password = forms.CharField(max_length=100)
