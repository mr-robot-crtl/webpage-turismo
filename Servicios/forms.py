from django import forms
from . import models


class PlaceTourForm(forms.ModelForm):
    class Meta:
        model=models.Place_Tour
        fields=['name','price','description','place_image']

class GuiaTourForm(forms.ModelForm):
    class Meta:
        model=models.Guia_tour
        fields=['name','decriptions','picture']

class MovilidadForm(forms.ModelForm):
    class Meta:
        model=models.Movilidad
        fields=['name','descriptions']




