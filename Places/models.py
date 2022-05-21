from django.db import models

# Create your models here.
class Lugares(models.Model):
    nombre=models.CharField(max_length=100)
    image=models.ImageField(upload_to='categoria-servicios', null=True, blank=True)
    descripcion=models.CharField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name='lugar'
        verbose_name_plural='lugares'  
    def __str__(self):
        return self.nombre
