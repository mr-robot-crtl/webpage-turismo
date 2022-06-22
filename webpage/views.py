from django.shortcuts import render,redirect, HttpResponse
from requests import request
from django.core.mail import send_mail


from django.conf import settings

from servicios.models import Guia_tour




from . import forms,models



# Create your views here.

def home(request):
    return render(request, "webpage/home.html")

def about_pucallpa(request):
    return render(request, "webpage/about-pucallpa.html")

def diccionario_selva(request):
    return render(request, "webpage/diccionario_selva.html")



def send_feedback_view(request):
    feedbackForm=forms.FeedbackForm()
    if request.method == 'POST':
        feedbackForm = forms.FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            feedbackForm.save()
            return render(request, 'webpage/feedback_sent.html')
    return render(request, 'webpage/send_feedback.html', {'feedbackForm':feedbackForm})

#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START --------------------
#---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request,'webpage/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'webpage/contactussuccess.html')
    return render(request, 'webpage/contactus.html', {'form':sub})
