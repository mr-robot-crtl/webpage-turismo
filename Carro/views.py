from django.shortcuts import render
from .carro import Carro
from Servicios.models import CategoriaServicio
from django.shortcuts import redirect

# Create your views here.
def agregar(request, categoriaservicio_id):
    carro=Carro(request)
    categoriaservicio=CategoriaServicio.objects.get(id=categoriaservicio_id)
    carro.agregar(categoriaservicio=categoriaservicio)
    return redirect("Servicio")

def eliminar(request, categoriaservicio_id):
    carro=Carro(request)
    categoriaservicio=CategoriaServicio.objects.get(id=categoriaservicio_id)
    carro.eliminar(categoriaservicio=categoriaservicio)
    return redirect("Servicio")

def restar(request, categoriaservicio_id):
    carro=Carro(request)
    categoriaservicio=CategoriaServicio.objects.get(id=categoriaservicio_id)
    carro.restar(categoriaservicio=categoriaservicio)
    return redirect("Servicio")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Servicio")

