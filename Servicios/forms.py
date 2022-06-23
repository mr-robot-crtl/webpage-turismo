from django import forms
from . import models


class PlaceTourForm(forms.ModelForm):
    class Meta:
        model=models.Place_Tour
        fields=['name','price','price_menor' ,'description','place_image','place']

class GuiaTourForm(forms.ModelForm):
    class Meta:
        model=models.Guia_tour
        fields=['name','decriptions','picture']

class MovilidadForm(forms.ModelForm):
    class Meta:
        model=models.Movilidad
        fields=['name','descriptions']




