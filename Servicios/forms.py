from django import forms
from . import models

class ServicioForm(forms.ModelForm):
    class Meta:
        model=models.Servicio
        fields=['name','price','description','servicio_image']

##dirección de envío

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#para la página de contacto
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
