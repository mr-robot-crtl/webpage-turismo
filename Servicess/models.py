from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from turtle import update
from venv import create
from django.db import models

# Create your models here.

class Services(models.Model):
    nombre_service=models.CharField(max_length=100)
    descripcion_service=models.CharField(max_length=200)
    costo_service=models.CharField(max_length=5)
    image_service=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name='service'
        verbose_name_plural='services'  
    def __str__(self):
        return self.nombre_service 