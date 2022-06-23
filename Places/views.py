import imp
from django.shortcuts import render, HttpResponse
from .models import Detail_Place, Place, Category_Place

# Create your views here.
def category_places(request):
    category=Category_Place.objects.all()
    return render(request,'placess/categorias_place.html',{'category':category})

def placess(request, category_id):
    category=Category_Place.objects.get(id=category_id)
    place=Place.objects.filter(category=category)
    return render(request, "placess/placess.html",{"place":place,'category':category})


def detail_place(request, place_id):
    place=Place.objects.get(id=place_id)
    details=Detail_Place.objects.filter(place=place)
    return render(request, "placess/detail_places.html",{"place":place,'details':details})



