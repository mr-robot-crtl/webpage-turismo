from django import forms
from . import models

class PlaceForm(forms.ModelForm):
    class Meta:
        model=models.Place
        fields=['name','lugar_image','descriptions','category']    


class DetailPlaceForm(forms.ModelForm):
    class Meta:
        model=models.Detail_Place
        fields=['name','descriptions', 'image_one','image_two','image_three','image_four','image_five','image_six','image_recommen','recommendation','ubicacion','place']    

class CategoryPlaceForm(forms.ModelForm):
    class Meta:
        model=models.Category_Place
        fields=['name','cat_lug_image']    


