from django.shortcuts import render, redirect
from uauth.forms import UserRegisterForm, UserLoginForm
from uauth.models import User
from wallet.models import AppTransaction, Wallet
from wallet.utils import generate_wallet_id
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login')
def index_view(request):
    return render(request, 'uauth/index.html')


def logout_view(request):
    logout(request)
    return redirect('login_url')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = User(phone_number=form.cleaned_data['phone_number'])
                    user.set_password(form.cleaned_data['password1'])
                    user.save()
                    while True:
                        wallet_id = generate_wallet_id()
                        if Wallet.objects.filter(wallet_id=wallet_id).count() == 0:
                            Wallet.objects.create(wallet_id=wallet_id, user=user)
                            break
                    login(request, user)
                    return redirect('index_url')
                except Exception as e:
                    print(e)
    return render(request, 'uauth/register_form.html')


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('index_url')
    return render(request, 'uauth/login_form.html')
