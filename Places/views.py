from django.shortcuts import render, HttpResponse

# Create your views here.

def places(request):
     return render(request, "Places/places.html")
def place_cat_aventu(request):
    return render(request, "cat_aventura/place_cat_aventu.html")
def lug_cat_aventu_lug_01(request):
    return render(request, "cat_aventura/lug_cat_aventu_lug_01.html")
def lug_cat_aventu_lug_02(request):
    return render(request, "cat_aventura/lug_cat_aventu_lug_02.html")

def lug_cat_turismo(request):
    return render(request, "cat_Turismo/lug_cat_turismo.html")

def lug_cat_turismo_lug_01(request):
    return render(request, "cat_Turismo/lug_cat_turismo_lug_01.html")

def lug_cat_turismo_lug_02(request):
    return render(request, "cat_Turismo/lug_cat_turismo_lug_02.html")