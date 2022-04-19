from django.shortcuts import render, HttpResponse

# Create your views here.
#CREAMOS LA FUNCION PARA RENDERISAR EL TEMPLATE HTML, QUE SERA LLAMADO DESDE urls.py
def tours(request):
     return render(request, "Tours/tours.html")
def tour_dia(request):
    return render(request, "Tours/tour_dia.html")
