import imp
from django.shortcuts import render
from Servicess.models import Services
# Create your views here.
def services(request):
     service=Services.objects.all()
     return render(request, "Servicess/services.html", {"service": service})
