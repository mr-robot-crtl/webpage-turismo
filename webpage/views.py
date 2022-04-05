from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "webpage/home.html")

def miniguia(request):
     return render(request, "webpage/miniGuia.html")

def lugares(request):
     return render(request, "webpage/lugares.html")

def login(request):
    return render(request, "webpage/login.html")