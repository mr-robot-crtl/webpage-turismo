from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "webpageApp/home.html")

def miniguia(request):
     return render(request, "webpageApp/miniGuia.html")

def lugares(request):
     return render(request, "webpageApp/lugares.html")

def login(request):
    return render(request, "webpageApp/login.html")