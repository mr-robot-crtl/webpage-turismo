
from pyexpat import model
from re import S
from telnetlib import SE
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from Places.models import Category_Place, Place
from webpage.models import Guia_tour
# Create your models here.

'''class Guia_tour(models.Model):
    name=models.CharField(max_length=40)
    decriptions=models.CharField(max_length=40)
    picture=models.ImageField(upload_to='guia_image/')
    def __str__(self):
        return self.name'''

'''class Servicio(models.Model):
    name=models.CharField(max_length=40)
    servicio_image= models.ImageField(upload_to='servicio_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Detail_servicio(models.Model):
    name=models.CharField(max_length=40)
    detail=models.CharField(max_length=40)
    recommendation=models.CharField(max_length=40)
    servicio=models.OneToOneField(Servicio, null=True, on_delete=models.SET_NULL)
    guia_tour=models.ForeignKey(Guia_tour, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name'''


'''class Pack_Tour(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    pack_image= models.ImageField(upload_to='pack_tour_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    category=models.OneToOneField(Category_Place,null=True, on_delete=models.SET_NULL)
    place_one=models.CharField(max_length=100)
    place_two=models.CharField(max_length=100)
    place_three=models.CharField(max_length=100)
    place_four=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Detail_Pack_Tour(models.Model):
    name=models.CharField(max_length=40)
    detail=models.CharField(max_length=100)
    recommendation=models.CharField(max_length=100)
    pack_tour=models.OneToOneField(Pack_Tour, null=True, on_delete=models.SET_NULL)
    guia_tour=models.ForeignKey(Guia_tour, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name'''


class Place_Tour(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    place_image= models.ImageField(upload_to='place_tour_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    category=models.OneToOneField(Category_Place,null=True, on_delete=models.SET_NULL)
    place=models.ForeignKey(Place,null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
        
class Detail_Place_Tour(models.Model):
    name=models.CharField(max_length=40)
    de_place_image= models.ImageField(upload_to='detail_place_tour_image/',null=True,blank=True)
    detail=models.CharField(max_length=100)
    recommendation=models.CharField(max_length=100)
    place_tour=models.OneToOneField(Place_Tour, null=True, on_delete=models.SET_NULL)
    guia_tour=models.ForeignKey(Guia_tour, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name





