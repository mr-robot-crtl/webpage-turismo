from django import forms
from . import models


class PlaceTourForm(forms.ModelForm):
    class Meta:
        model=models.Place_Tour
        fields=['name','price','description','place_image']


