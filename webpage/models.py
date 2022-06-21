from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name


class Guia_tour(models.Model):
    name=models.CharField(max_length=40)
    decriptions=models.CharField(max_length=40)
    picture=models.ImageField(upload_to='guia_image/')
    def __str__(self):
        return self.name
