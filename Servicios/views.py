import imp
from django.shortcuts import render,redirect,reverse
from . import forms,models
from login.views import is_cliente
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings

def home_view(request):
    servicios=models.Servicio.objects.all()
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'ecom/index.html',{'servicios':servicios,'servicio_count_in_cart':servicio_count_in_cart})


#for showing login button for admin(by sumit)

#---------------------------------------------------------------------------------
#------------------------ PUBLIC CLIENTE RELATED VIEWS START ---------------------
#---------------------------------------------------------------------------------
def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    servicios=models.Servicio.objects.all().filter(name__icontains=query)
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'ecom/cliente_home.html',{'servicios':servicios,'word':word,'servicio_count_in_cart':servicio_count_in_cart})
    return render(request,'ecom/index.html',{'servicios':servicios,'word':word,'servicio_count_in_cart':servicio_count_in_cart})


# any one can add servicio to cart, no need of signin
def add_to_cart_view(request,pk):
    servicios=models.Servicio.objects.all()

    #for cart counter, fetching servicios ids added by cliente from cookies
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=1

    response = render(request, 'ecom/index.html',{'servicios':servicios,'servicio_count_in_cart':servicio_count_in_cart})

    #adding servicio id to cookies
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        if servicio_ids=="":
            servicio_ids=str(pk)
        else:
            servicio_ids=servicio_ids+"|"+str(pk)
        response.set_cookie('servicio_ids', servicio_ids)
    else:
        response.set_cookie('servicio_ids', pk)

    servicio=models.Servicio.objects.get(id=pk)
    messages.info(request, servicio.name + ' added to cart successfully!')

    return response



# for checkout of cart
def cart_view(request):
    #for cart counter
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0

    # fetching servicio details from db whose id is present in cookie
    servicios=None
    total=0
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        if servicio_ids != "":
            servicio_id_in_cart=servicio_ids.split('|')
            servicios=models.Servicio.objects.all().filter(id__in = servicio_id_in_cart)

            #for total price shown in cart
            for p in servicios:
                total=total+p.price
    return render(request,'ecom/cart.html',{'servicios':servicios,'total':total,'servicio_count_in_cart':servicio_count_in_cart})


def remove_from_cart_view(request,pk):
    #for counter in cart
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0

    # removing servicio id from cookie
    total=0
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        servicio_id_in_cart=servicio_ids.split('|')
        servicio_id_in_cart=list(set(servicio_id_in_cart))
        servicio_id_in_cart.remove(str(pk))
        servicios=models.Servicio.objects.all().filter(id__in = servicio_id_in_cart)
        #for total price shown in cart after removing servicio
        for p in servicios:
            total=total+p.price

        #  for update coookie value after removing servicio id in cart
        value=""
        for i in range(len(servicio_id_in_cart)):
            if i==0:
                value=value+servicio_id_in_cart[0]
            else:
                value=value+"|"+servicio_id_in_cart[i]
        response = render(request, 'ecom/cart.html',{'servicios':servicios,'total':total,'servicio_count_in_cart':servicio_count_in_cart})
        if value=="":
            response.delete_cookie('servicio_ids')
        response.set_cookie('servicio_ids',value)
        return response


def send_feedback_view(request):
    feedbackForm=forms.FeedbackForm()
    if request.method == 'POST':
        feedbackForm = forms.FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            feedbackForm.save()
            return render(request, 'ecom/feedback_sent.html')
    return render(request, 'ecom/send_feedback.html', {'feedbackForm':feedbackForm})


#---------------------------------------------------------------------------------
#------------------------ CLIENTE RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START --------------------
#---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request,'ecom/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'ecom/contactussuccess.html')
    return render(request, 'ecom/contactus.html', {'form':sub})

def afterlogin_view(request):
    if is_cliente(request.user):
        return redirect('cliente-home')
    else:
        return redirect('admin-dashboard')
