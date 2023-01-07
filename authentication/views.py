from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from authentication.forms import LoginForm

def login_user(reqest):
    context = {'login_form': LoginForm()}
    if reqest.method == 'POST':
        login_form = LoginForm(reqest.POST)  # data from form
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(reqest, user)
                return redirect('index')
    return render(reqest, 'auth/login.html', context)

def register(reqest):
    return render(reqest, 'auth/register.html')

def logout_user(reqest):
    logout(reqest)
    return redirect('index')