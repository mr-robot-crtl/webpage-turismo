from pydoc import importfile
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
#def login(request):
 #   return render(request, "Login/login.html")

class Registro(View):
    #La encargada de mostrar el formulario
    def get(self, request):
        form=UserCreationForm()
        return render(request, "Login/registro.html",{"form":form})
    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect("Home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "Login/registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no valido")
        else:
             messages.error(request, "Informacion incorrecta")

    form=AuthenticationForm()
    return render(request, "Login/login.html",{"form":form})
        
    


 