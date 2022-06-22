from email.mime import image
from unicodedata import category, name
from django.db import models


# Create your models here.
class Category_Place(models.Model):
    name=models.CharField(max_length=40)
    cat_lug_image= models.ImageField(upload_to='cat_lug_image/',null=True,blank=True)
    def __str__(self):
        return self.name

class Place(models.Model):
    name=models.CharField(max_length=40,unique=True)
    lugar_image= models.ImageField(upload_to='lugar_image/',null=True,blank=True)
    descriptions=models.CharField(max_length=500)
    category=models.ForeignKey(Category_Place, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Detail_Place(models.Model):
    name=models.CharField(max_length=40)
    descriptions=models.CharField(max_length=500)
    detail_image= models.ImageField(upload_to='detail_lugar_image/',null=True,blank=True)
    image_one=models.ImageField(upload_to='Galeria_image_Place/',null=True,blank=True)
    image_two=models.ImageField(upload_to='Galeria_image_Place/',null=True,blank=True)
    image_three=models.ImageField(upload_to='Galeria_image_Place/',null=True,blank=True)
    image_four=models.ImageField(upload_to='Galeria_image_Place/',null=True,blank=True)
    image_five=models.ImageField(upload_to='Galeria_image_Place/',null=True,blank=True)
    image_six=models.ImageField(upload_to='Galeria_image_Place/',null=True,blank=True)
    image_recommen=models.ImageField(upload_to='Image_recommen/',null=True,blank=True)
    recommendation=models.CharField(max_length=500)
    ubicacion=models.CharField(max_length=500)
    place=models.OneToOneField(Place, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

