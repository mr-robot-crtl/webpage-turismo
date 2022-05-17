import imp
from django.shortcuts import render
from Servicios.models import PlanServicio, CategoriaServicio
# Create your views here.

def servicio(request):
     categoria=CategoriaServicio.objects.all()
     return render(request, "Servicios/services.html", {"categoria": categoria})

def planServicio(request,):
     plan=PlanServicio.objects.all()
     return render(request, "Servicios/planServicio.html", {"plan": plan})



     #plan=PlanServicio.objects.all()
     #return render(request, "Servicess/planServicio.html", {"plan": plan})


def categoriaServicio(request, planservicio_id):
     plan=PlanServicio.objects.get(id=planservicio_id)
     categoria=CategoriaServicio.objects.filter(planes=plan)
     return render(request, "Servicios/categoriaServicio.html", {"categoria": categoria,"plan":plan})

     #categoria=CategoriaServicio.objects.all()
     #return render(request, "Servicios/categoriaServicio.html", {"categoria": categoria})

