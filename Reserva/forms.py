from django import forms
from . import models

class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    fecha= forms.DateField()
    num_a= forms.IntegerField()
    num_n= forms.IntegerField()

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']