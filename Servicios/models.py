
from pyexpat import model
from re import S
from telnetlib import SE
from tkinter import CASCADE
from tkinter.tix import Tree
from typing_extensions import Required
from unicodedata import category
from django.db import models
from Places.models import Category_Place, Place
# Create your models here.

class Guia_tour(models.Model):
    name=models.CharField(max_length=40)
    decriptions=models.CharField(max_length=500)
    picture=models.ImageField(upload_to='guia_image/')
    def __str__(self):
        return self.name

class Movilidad(models.Model):
    name=models.CharField(max_length=40)
    descriptions=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Place_Tour(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=1000)
    place_image= models.ImageField(upload_to='place_tour_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    price_menor = models.PositiveIntegerField()
    place=models.ForeignKey(Place,null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
        
class Detail_Place_Tour(models.Model):
    STATUS =(
        ('Yes','Yes'),
        ('No','No'),
    )
    name=models.CharField(max_length=40)
    de_place_image= models.ImageField(upload_to='detail_place_tour_image/',null=True,blank=True)
    detail=models.CharField(max_length=150)
    recommendation=models.CharField(max_length=150)
    place_tour=models.OneToOneField(Place_Tour, null=True, on_delete=models.SET_NULL)
    guia_tour=models.ForeignKey(Guia_tour, null=True, on_delete=models.SET_NULL)
    status_movilidad=models.CharField(max_length=50,null=True,choices=STATUS)
    movilidad=models.ForeignKey(Movilidad,blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name





