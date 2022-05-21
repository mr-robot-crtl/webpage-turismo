from ast import If
from ctypes import FormatError
import imp
from django.shortcuts import redirect, render
from Servicios.models import PlanServicio, CategoriaServicio, DetalleCategoria
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def servicio(request):
     plan=PlanServicio.objects.all()
     formulario_contacto=FormularioContacto()
     if request.method=="POST":
          formulario_contacto=FormularioContacto(data=request.POST)
          if formulario_contacto.is_valid():
               nombre=request.POST.get("nombre")
               email=request.POST.get("email")
               contenido=request.POST.get("contenido")

               email=EmailMessage("Mensaje desde app Django", 
               "EL usuarrio con nombre {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
               "",["juancitodelbarrio47@gmail.com"],reply_to=[email])

               try:
                    email.send()
                    return redirect("/servicio/?valido")
               except:
                    return redirect("/servicio/?novalido")

     return render(request, "Servicios/services.html", {"plan": plan, 'miFormulario':formulario_contacto})

def planServicio(request,):
     plan=PlanServicio.objects.all()
     return render(request, "Servicios/planServicio.html", {"plan": plan})

def categoriaServicio(request, planservicio_id):
     plan=PlanServicio.objects.get(id=planservicio_id)
     categoria=CategoriaServicio.objects.filter(planes=plan)
     return render(request, "Servicios/categoriaServicio.html", {"categoria": categoria,"plan":plan})

def detalleCategoria(request, categoriaservicio_id):
     categoria=CategoriaServicio.objects.get(id=categoriaservicio_id)
     detalle=DetalleCategoria.objects.filter(categorias=categoria)
     return render(request, "Servicios/detalle_categoria.html", {"detalle": detalle,"categoria":categoria})


    