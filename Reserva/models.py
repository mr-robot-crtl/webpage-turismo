from django.db import models
from login.models import Cliente
from servicios.models import Place_Tour

# Create your models here.

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE,null=True)
    place_tour=models.ForeignKey(Place_Tour, on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)

    mobile = models.CharField(max_length=20,null=True)

    fecha = models.DateField(auto_now = False)

    num_a = models.IntegerField()
    num_n = models.IntegerField()


    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
