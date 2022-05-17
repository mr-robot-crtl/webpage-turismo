from doctest import OutputChecker
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from Servicios.models import CategoriaServicio
from django.db.models import F, Sum, FloatField
# Create your models here.
User=get_user_model
class Reserva(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    @property
    def total(self):
        return self.lineareserva_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total                                                                                                                                "]

    class Meta:
        db_table='reserva'
        verbose_name='reserva'
        verbose_name_plural='reservas'
        ordering=['id']

class LineaReserva(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    categoriaservicio_id=CategoriaServicio.ForeignKey(User, on_delete=models.CASCADE)
    reserva_id=models.ForeignKey(Reserva, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.categoriaservicio_id.nombre}'

    class Meta:
        db_table='lineareserva'
        verbose_name='lineareserva'
        verbose_name_plural='lineasreservas'
        ordering=['id']

