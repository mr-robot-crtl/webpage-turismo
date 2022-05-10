from pyexpat import model
from tabnanny import verbose
from turtle import update
from venv import create
from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre_servicio=models.CharField(max_length=100)
    descripcion_servicio=models.CharField(max_length=200)
    costo_servicio=models.CharField(max_length=5)
    image_servicio=models.ImageField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'  
    def __str__(self):
        return self.nombre_servicio 