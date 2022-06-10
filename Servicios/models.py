
from pyexpat import model
from re import S
from telnetlib import SE
from tkinter import CASCADE
from django.db import models
# Create your models here.

class Guia_tour(models.Model):
    name=models.CharField(max_length=40)
    decriptions=models.CharField(max_length=40)
    picture=models.ImageField(upload_to='guia_image/')
    def __str__(self):
        return self.name


class Detail_servicio(models.Model):
    name=models.CharField(max_length=40)
    detail=models.CharField(max_length=40)
    recommendation=models.CharField(max_length=40)
    guia_tour=models.ForeignKey(Guia_tour, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name


class Servicio(models.Model):
    name=models.CharField(max_length=40)
    servicio_image= models.ImageField(upload_to='servicio_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    detail_servicio=models.OneToOneField(Detail_servicio, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name



class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
