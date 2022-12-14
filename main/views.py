from django.shortcuts import render

def index(reqest):
    return render(reqest, 'index.html')

def about(reqest):
    return render(reqest, 'about.html')