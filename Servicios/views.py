import imp
from tkinter import Pack
from django.shortcuts import render,redirect

from Places.models import Place
from . import forms,models
from login.views import is_cliente
from django.http import HttpResponseRedirect,HttpResponse
from .models import Guia_tour, Place_Tour, Detail_Place_Tour

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages




'''def home_view_pack(request):
    packs=models.Pack_Tour.objects.all()
    if 'pack_ids' in request.COOKIES:
        pack_ids = request.COOKIES['pack_ids']
        counter=pack_ids.split('|')
        pack_count_in_cart=len(set(counter))
    else:
        pack_count_in_cart=0
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'servicios/pack_tour.html',{'packs':packs,'pack_count_in_cart':pack_count_in_cart})


#for showing login button for admin(by sumit)

#---------------------------------------------------------------------------------
#------------------------ PUBLIC CLIENTE RELATED VIEWS START ---------------------
#---------------------------------------------------------------------------------

def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    servicios=models.Place_Tour.objects.all().filter(name__icontains=query)
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'login/cliente_home.html',{'servicios':servicios,'word':word,'servicio_count_in_cart':servicio_count_in_cart})
    return render(request,'servicios/servicios.html',{'servicios':servicios,'word':word,'servicio_count_in_cart':servicio_count_in_cart})

# any one can add servicio to cart, no need of signin
def add_to_cart_view(request,pk):
    packs=models.Pack_Tour.objects.all()
    #for cart counter, fetching servicios ids added by cliente from cookies
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=1

    response = render(request, 'servicios/servicios.html',{'packs':packs,'servicio_count_in_cart':servicio_count_in_cart})

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

    return response

# any one can add servicio to cart, no need of signin
def add_to_cart_view_pack(request,pk):
    packs=models.Pack_Tour.objects.all()
    #for cart counter, fetching servicios ids added by cliente from cookies
    if 'pack_ids' in request.COOKIES:
        pack_ids = request.COOKIES['pack_ids']
        counter=pack_ids.split('|')
        pack_count_in_cart=len(set(counter))
    else:
        pack_count_in_cart=1

    response = render(request, 'servicios/pack_tour.html',{'packs':packs,'pack_count_in_cart':pack_count_in_cart})

    #adding servicio id to cookies
    if 'pack_ids' in request.COOKIES:
        pack_ids = request.COOKIES['pack_ids']
        if pack_ids=="":
            pack_ids=str(pk)
        else:
            pack_ids=pack_ids+"|"+str(pk)
        response.set_cookie('pack_ids', pack_ids)
    else:
        response.set_cookie('pack_ids', pk)
    pack=models.Pack_Tour.objects.get(id=pk)
    messages.info(request, pack.name + ' added to cart successfully!')

    return response 


# for checkout of cart
def cart_view_pack(request):
    #for cart counter

    if 'pack_ids'in request.COOKIES:
        pack_ids = request.COOKIES['pack_ids']
        counter=pack_ids.split('|')
        pack_count_in_cart=len(set(counter))
    else:
        pack_count_in_cart=0
    # fetching servicio details from db whose id is present in cookie
    packs=None
    total=0
 
    

    if 'pack_ids'in request.COOKIES:
        pack_ids = request.COOKIES['pack_ids']
        if pack_ids != "":
            pack_id_in_cart=pack_ids.split('|')
            packs=models.Pack_Tour.objects.all().filter(id__in = pack_id_in_cart)

            #for total price shown in cart
            for p in packs:
                total=total+p.price


    return render(request,'servicios/cart_pack.html',{'packs':packs,'total':total,'pack_count_in_cart':pack_count_in_cart})



        
    
def remove_from_cart_view_pack(request,pk):
    #for counter in cart
    if 'pack_ids' in request.COOKIES:
        pack_ids = request.COOKIES['pack_ids']
        counter=pack_ids.split('|')
        pack_count_in_cart=len(set(counter))
    else:
        pack_count_in_cart=0
    # removing servicio id from cookie
    total=0
    if 'pack_ids' in request.COOKIES:
        pack_ids = request.COOKIES['pack_ids']
        pack_id_in_cart=pack_ids.split('|')
        pack_id_in_cart=list(set(pack_id_in_cart))
        pack_id_in_cart.remove(str(pk))
        packs=models.Pack_Tour.objects.all().filter(id__in = pack_id_in_cart)

        #for total price shown in cart after removing servicio
        for p in packs:
            total=total+p.price

        #  for update coookie value after removing servicio id in cart
        value=""
        for i in range(len(pack_id_in_cart)):
            if i==0:
                value=value+pack_id_in_cart[0]
            else:
                value=value+"|"+pack_id_in_cart[i]
        response = render(request, 'servicios/cart_pack.html',{'packs':packs,'total':total,'pack_count_in_cart':pack_count_in_cart})
        if value=="":
            response.delete_cookie('pack_ids')
        response.set_cookie('pack_ids',value)
        return response'''


################################################################################################




def home_view(request):
    servicios=models.Place_Tour.objects.all()
    menor_price=0
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    for p in servicios:
        menor_price=p.price/2
    else:
        servicio_count_in_cart=0
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'servicios/servicios.html',{'servicios':servicios,'menor_price':menor_price,'servicio_count_in_cart':servicio_count_in_cart})


#for showing login button for admin(by sumit)

#---------------------------------------------------------------------------------
#------------------------ PUBLIC CLIENTE RELATED VIEWS START ---------------------
#---------------------------------------------------------------------------------
def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    servicios=models.Place_Tour.objects.all().filter(name__icontains=query)
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'login/cliente_home.html',{'servicios':servicios,'word':word,'servicio_count_in_cart':servicio_count_in_cart})
    return render(request,'servicios/servicios.html',{'servicios':servicios,'word':word,'servicio_count_in_cart':servicio_count_in_cart})


# any one can add servicio to cart, no need of signin
def add_to_cart_view(request,pk):
    servicios=models.Place_Tour.objects.all()
    #for cart counter, fetching servicios ids added by cliente from cookies
    if 'servicio_ids' in request.COOKIES:

        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else: 
        servicio_count_in_cart=1

    response = render(request, 'servicios/servicios.html',{'servicios':servicios,'servicio_count_in_cart':servicio_count_in_cart})
 
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
    servicio=models.Place_Tour.objects.get(id=pk)
    messages.info(request, servicio.name + ' added to cart successfully!')

    return response



# for checkout of cart
def cart_view(request):
    #for cart counter

    if 'servicio_ids'in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0
    # fetching servicio details from db whose id is present in cookie
    servicios=None
    total=0
    if 'servicio_ids'in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        if servicio_ids != "":
            servicio_id_in_cart=servicio_ids.split('|')
            servicios=models.Place_Tour.objects.all().filter(id__in = servicio_id_in_cart)
            #for total price shown in cart
            for p in servicios:
                total=total+p.price

###############PACK############################################################################
    #for cart counter

    return render(request,'servicios/cart.html',{'servicios':servicios,'total':total,'servicio_count_in_cart':servicio_count_in_cart})


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
        servicios=models.Place_Tour.objects.all().filter(id__in = servicio_id_in_cart)
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
        response = render(request, 'servicios/cart.html',{'servicios':servicios,'total':total,'servicio_count_in_cart':servicio_count_in_cart})
        if value=="":
            response.delete_cookie('servicio_ids')
        response.set_cookie('servicio_ids',value)
        return response
        

def afterlogin_view(request):
    if is_cliente(request.user):
        return redirect('cliente-home')
    else:
        return redirect('admin-dashboard')


@login_required(login_url='clientelogin')
@user_passes_test(is_cliente)
def cliente_home_view(request):

    servicios=Place_Tour.objects.all()
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0
    return render(request,'servicios/servicios.html',{'servicios':servicios,'servicio_count_in_cart':servicio_count_in_cart})


def detail(request, place_tour_id):
    places=Place_Tour.objects.get(id=place_tour_id)
    details=Detail_Place_Tour.objects.filter(place_tour=places)
    return render(request, "servicios/detail.html",{"details":details,'places':places})



'''def services(request):
    pack=Pack_Tour.objects.all()
    place_tour=Place_Tour.objects.all()
    return render(request,'servicios/pack_tour.html',{'pack':pack,'place_tour':place_tour})

def detail_pack(request, pack_tour_id):
    pack=Pack_Tour.objects.get(id=pack_tour_id)
    detail_pack=Detail_Pack_Tour.objects.filter(pack_tour=pack)
    return render(request, "servicios/detail_packs.html",{"detail_pack":detail_pack,'pack':pack})'''

def tour_place(request):
    place_tour=Detail_Place_Tour.objects.all()
    return render(request,'servicios/place_tour.html',{'place_tour':place_tour})

'''def placess(request, category_id):
    category=Category_Place.objects.get(id=category_id)
    place=Place.objects.filter(category=category)
    return render(request, "placess/placess.html",{"place":place,'category':category})'''



