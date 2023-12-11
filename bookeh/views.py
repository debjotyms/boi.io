from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'pages/home.html')

def cart(request):
    return render(request, 'pages/cart.html')