from django import forms
from . import models

class ServicioForm(forms.ModelForm):
    class Meta:
        model=models.Servicio
        fields=['name','price','description','servicio_image']


