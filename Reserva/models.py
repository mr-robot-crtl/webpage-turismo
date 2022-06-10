from django.db import models
from login.models import Cliente
from servicios.models import Servicio

# Create your models here.

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE,null=True)
    servicio=models.ForeignKey(Servicio, on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)

    fecha = models.DateField(auto_now = False)

    num_a = models.IntegerField()
    num_n = models.IntegerField(null = True)


    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

'''class reservacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=True)
    habitacion = models.ForeignKey(Servicio,  on_delete=models.CASCADE,null=True)
    fechaCrea = models.DateTimeField(auto_now = True)
    fecha = models.DateField(verbose_name = 'Fecha',auto_now = False)
    num_a = models.IntegerField(verbose_name = 'Numero de adultos')
    num_n = models.IntegerField(verbose_name = 'Numero de ninios', null = True)
    
    class Meta:
        verbose_name = u'Reservacion'
        verbose_name_plural = u'Reservaciones'''

    
