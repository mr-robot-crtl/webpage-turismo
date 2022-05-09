from django.shortcuts import render, HttpResponse

# Create your views here.

def places(request):
     return render(request, "Places/places.html")
def place_cat_aventu(request):
    return render(request, "Places/place_cat_aventu.html")
def lug_cat_aventu_lug_01(request):
    return render(request, "Places/lug_cat_aventu_lug_01.html")
