from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "webpage/home.html")

def tours(request):
     return render(request, "webpage/tours.html")

def places(request):
     return render(request, "webpage/places.html")

def login(request):
    return render(request, "webpage/login.html")