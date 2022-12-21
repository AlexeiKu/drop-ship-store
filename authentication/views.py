from django.contrib.auth import logout
from django.shortcuts import render, redirect


def login_user(reqest):
    return render(reqest, 'auth/login.html')

def register(reqest):
    return render(reqest, 'auth/register.html')

def logout_user(reqest):
    logout(reqest)
    return redirect('index')