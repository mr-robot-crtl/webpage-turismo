from distutils.command.upload import upload
from email.mime import image
from mailbox import NoSuchMailboxError
from pyexpat import model
from ssl import create_default_context
from tabnanny import verbose
from turtle import update
from venv import create
from django.db import models

# Create your models here.
class PlanServicio(models.Model):
    nombre=models.CharField(max_length=50)
    image=models.ImageField(upload_to='plan-servicio', null=True, blank=True)
    descripcion=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='plan'
        verbose_name_plural='planes'  
    def __str__(self):
        return self.nombre
    

class Movilidad(models.Model):
    nombre=models.CharField(max_length=100)
    image=models.ImageField(upload_to='movilidad', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name='movilidad'
        verbose_name_plural='movilidades'  
    def __str__(self):
        return self.nombre

class CategoriaServicio(models.Model):
    nombre=models.CharField(max_length=100)
    image=models.ImageField(upload_to='categoria-servicios', null=True, blank=True)
    descripcion=models.CharField(max_length=200)
    costo=models.FloatField()
    #Relacionando con la tabla CategoriaServ
    planes=models.ManyToManyField(PlanServicio)
    #categorias=models.ForeignKey(CategoriaServ, on_delete=models.CASCADE)
    movilidad=models.ForeignKey(Movilidad, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'  
    def __str__(self):
        return self.nombre
