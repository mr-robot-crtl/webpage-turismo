from calendar import TextCalendar
from django import forms
from django.contrib.auth.models import User
from . import models

class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    fecha= forms.DateField()
    num_a= forms.IntegerField()
    num_n= forms.IntegerField()
    Address = forms.CharField(max_length=500)