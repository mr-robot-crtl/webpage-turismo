
from django.db import models
# Create your models here.
class Servicio(models.Model):
    name=models.CharField(max_length=40)
    servicio_image= models.ImageField(upload_to='servicio_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
