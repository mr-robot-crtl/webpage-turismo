from django.shortcuts import render, HttpResponse
from requests import request

from Carro.carro import Carro

# Create your views here.

def home(request):
    carro=Carro(request)
    return render(request, "webpage/home.html")

def about_pucallpa(request):
    return render(request, "webpage/about-pucallpa.html")
