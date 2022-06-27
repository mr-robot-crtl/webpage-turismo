from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,user_passes_test
from Places.form import CategoryPlaceForm, DetailPlaceForm, PlaceForm
from Places.models import Category_Place, Detail_Place, Place
from webpage.models import Feedback
from reserva.models import Orders
from login.models import Cliente, User
from login.forms import ClienteForm, ClienteUserForm
from servicios.models import Guia_tour, Movilidad, Place_Tour
from servicios.forms import GuiaTourForm, MovilidadForm, PlaceTourForm


# Create your views here.
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
    clientecount=Cliente.objects.all().count()
    serviciocount=Place_Tour.objects.all().count()
    ordercount=Orders.objects.all().count()

    # for recent order tables
    orders=Orders.objects.all()
    ordered_servicios=[]
    ordered_bys=[]
    for order in orders:
        ordered_servicio=Place_Tour.objects.all().filter(id=order.place_tour.id)
        ordered_by=Cliente.objects.all().filter(id = order.cliente.id)
        ordered_servicios.append(ordered_servicio)
        ordered_bys.append(ordered_by)

    mydict={
    'clientecount':clientecount,
    'serviciocount':serviciocount,
    'ordercount':ordercount,
    'data':zip(ordered_servicios,ordered_bys,orders),
    }
    return render(request,'admins/admin_dashboard.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_view_booking_view(request):
    orders=Orders.objects.all()
    ordered_servicios=[]
    ordered_bys=[]
    for order in orders:
        ordered_servicio=Place_Tour.objects.all().filter(id=order.place_tour.id)
        ordered_by=Cliente.objects.all().filter(id = order.cliente.id)
        ordered_servicios.append(ordered_servicio)
        ordered_bys.append(ordered_by)
    return render(request,'admins/admin_view_booking.html',{'data':zip(ordered_servicios,ordered_bys,orders)})

# Create your views here.
#for showing login button for admin(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

##################################### CLIENTE ##########################################
# admin view cliente table
@login_required(login_url='adminlogin')
def view_cliente_view(request):
    clientes=Cliente.objects.all()
    return render(request,'admins/admin_cliente/view_cliente.html',{'clientes':clientes})

@login_required(login_url='adminlogin')
def view_user_view(request):
    users=User.objects.all()
    return render(request,'admins/admin_user.html',{'users':users})
# admin delete cliente
@login_required(login_url='adminlogin')
def delete_cliente_view(request,pk):
    cliente=Cliente.objects.get(id=pk)
    user=User.objects.get(id=cliente.user_id)
    user.delete()
    cliente.delete()
    return redirect('view-cliente')

@login_required(login_url='adminlogin')
def update_cliente_view(request,pk):
    cliente=Cliente.objects.get(id=pk)
    user=User.objects.get(id=cliente.user_id)
    userForm=ClienteUserForm(instance=user)
    clienteForm=ClienteForm(request.FILES,instance=cliente)
    mydict={'userForm':userForm,'clienteForm':clienteForm}
    if request.method=='POST':
        userForm=ClienteUserForm(request.POST,instance=user)
        clienteForm=ClienteForm(request.POST,instance=cliente)
        if userForm.is_valid() and clienteForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            clienteForm.save()
            return redirect('view-cliente')
    return render(request,'admins/admin_cliente/admin_update_cliente.html',context=mydict)

################################## GUIA TOUR #######################################
# admin view the guias tour
@login_required(login_url='adminlogin')
def admin_guias_tour(request):
    guias=Guia_tour.objects.all()
    return render(request,'admins/admin_guias_tour/admin_guias_tour.html',{'guias':guias})
    
# admin add guias by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_guia_view(request):
    guiaTourForm=GuiaTourForm
    if request.method=='POST':
        guiaTourForm=GuiaTourForm(request.POST, request.FILES)
        if guiaTourForm.is_valid():
            guiaTourForm.save()
        return HttpResponseRedirect('admin-guias-tour')
    return render(request,'admins/admin_guias_tour/admin_add_guias.html',{'guiaTourForm':guiaTourForm})

@login_required(login_url='adminlogin')
def delete_guia_view(request,pk):
    guia=Guia_tour.objects.get(id=pk)
    guia.delete()
    return redirect('admin-guias-tour')

@login_required(login_url='adminlogin')
def update_guia_view(request,pk):
    guia=Guia_tour.objects.get(id=pk)
    guiaTourForm=GuiaTourForm(instance=guia)
    if request.method=='POST':
        guiaTourForm=GuiaTourForm(request.POST,request.FILES,instance=guia)
        if guiaTourForm.is_valid():
            guiaTourForm.save()
            return redirect('admin-guias-tour')
    return render(request,'admins/admin_guias_tour/admin_update_guia.html',{'guiaTourForm':guiaTourForm})
################################## END #############################################

################################## MOVILIDAD #######################################
# admin view the guias tour
@login_required(login_url='adminlogin')
def admin_movilidad(request):
    movilidades=Movilidad.objects.all()
    return render(request,'admins/admin_movilidad/admin_movilidad.html',{'movilidades':movilidades})
    
# admin add guias by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_movilidad_view(request):
    movilidadForm=MovilidadForm
    if request.method=='POST':
        movilidadForm=MovilidadForm(request.POST, request.FILES)
        if movilidadForm.is_valid():
            movilidadForm.save()
        return HttpResponseRedirect('admin-movilidad')
    return render(request,'admins/admin_movilidad/admin_add_movilidad.html',{'movilidadForm':movilidadForm})

@login_required(login_url='adminlogin')
def delete_movilidad_view(request,pk):
    movilidad=Movilidad.objects.get(id=pk)
    movilidad.delete()
    return redirect('admin-movilidad')

@login_required(login_url='adminlogin')
def update_movilidad_view(request,pk):
    movilidad=Movilidad.objects.get(id=pk)
    movilidadForm=MovilidadForm(instance=movilidad)
    if request.method=='POST':
        movilidadForm=MovilidadForm(request.POST,request.FILES,instance=movilidad)
        if movilidadForm.is_valid():
            movilidadForm.save()
            return redirect('admin-movilidad')
    return render(request,'admins/admin_movilidad/admin_update_movilidad.html',{'movilidadForm':movilidadForm})
################################## END #############################################

#################################### CATEGORY PLACES ####################################
@login_required(login_url='adminlogin')
def admin_category_places(request):
    catplaces=Category_Place.objects.all()
    return render(request,'admins/category_places/admin_category_places.html',{'catplaces':catplaces})

# admin add guias by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_cat_place_view(request):
    catPlaceForm=CategoryPlaceForm
    if request.method=='POST':
        catPlaceForm=CategoryPlaceForm(request.POST, request.FILES)
        if catPlaceForm.is_valid():
            catPlaceForm.save()
        return HttpResponseRedirect('admin-cat-places')
    return render(request,'admins/category_places/admin_add_cat_places.html',{'catPlaceForm':catPlaceForm})

@login_required(login_url='adminlogin')
def delete_cat_place_view(request,pk):
    catPlace=Category_Place.objects.get(id=pk)
    catPlace.delete()
    return redirect('admin-cat-places')

@login_required(login_url='adminlogin')
def update_cat_place_view(request,pk):
    catPlace=Category_Place.objects.get(id=pk)
    catPlaceForm=CategoryPlaceForm(instance=catPlace)
    if request.method=='POST':
        catPlaceForm=CategoryPlaceForm(request.POST,request.FILES,instance=catPlace)
        if catPlaceForm.is_valid():
            catPlaceForm.save()
            return redirect('admin-cat-places')
    return render(request,'admins/category_places/admin_update_cat_places.html',{'catPlaceForm':catPlaceForm})

######################################## END ##############################################

################################## PLACES #######################################
# admin view the guias tour
@login_required(login_url='adminlogin')
def admin_places(request):
    places=Place.objects.all()
    return render(request,'admins/admin_places/admin_places.html',{'places':places})
    
# admin add guias by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_place_view(request):
    placeForm=PlaceForm
    if request.method=='POST':
        placeForm=PlaceForm(request.POST, request.FILES)
        if placeForm.is_valid():
            placeForm.save()
        return HttpResponseRedirect('admin-places')
    return render(request,'admins/admin_places/admin_add_places.html',{'placeForm':placeForm})

@login_required(login_url='adminlogin')
def delete_place_view(request,pk):
    place=Place.objects.get(id=pk)
    place.delete()
    return redirect('admin-places')

@login_required(login_url='adminlogin')
def update_place_view(request,pk):
    place=Place.objects.get(id=pk)
    placeForm=PlaceForm(instance=place)
    if request.method=='POST':
        placeForm=PlaceForm(request.POST,request.FILES,instance=place)
        if placeForm.is_valid():
            placeForm.save()
            return redirect('admin-places')
    return render(request,'admins/admin_places/admin_update_places.html',{'placeForm':placeForm})
################################## END #############################################



#################################### DETALLES PLACES ####################################
@login_required(login_url='adminlogin')
def admin_detalle_places(request):
    detplaces=Detail_Place.objects.all()
    return render(request,'admins/admin_detalle_places/admin_detalle_places.html',{'detplaces':detplaces})

# admin add guias by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_detalle_place_view(request):
    detPlaceForm=DetailPlaceForm
    if request.method=='POST':
        detPlaceForm=DetailPlaceForm(request.POST, request.FILES)
        if detPlaceForm.is_valid():
            detPlaceForm.save()
        return HttpResponseRedirect('admin-detalle-places')
    return render(request,'admins/admin_detalle_places/admin_add_detalle_places.html',{'detPlaceForm':detPlaceForm})

@login_required(login_url='adminlogin')
def delete_detalle_place_view(request,pk):
    detPlace=Detail_Place.objects.get(id=pk)
    detPlace.delete()
    return redirect('admin-detalle-places')

@login_required(login_url='adminlogin')
def update_detalle_place_view(request,pk):
    detPlace=Detail_Place.objects.get(id=pk)
    detPlaceForm=DetailPlaceForm(instance=detPlace)
    if request.method=='POST':
        detPlaceForm=DetailPlaceForm(request.POST,request.FILES,instance=detPlace)
        if detPlaceForm.is_valid():
            detPlaceForm.save()
            return redirect('admin-detalle-places')
    return render(request,'admins/admin_detalle_places/admin_update_detalle_places.html',{'detPlaceForm':detPlaceForm})

######################################## SERVICIOS ##############################################

# admin view the servicio
@login_required(login_url='adminlogin')
def admin_servicios_view(request):
    servicios=Place_Tour.objects.all()
    return render(request,'admins/admin_servicios/admin_servicios.html',{'servicios':servicios})
# admin add servicio by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_servicio_view(request):
    servicioForm=PlaceTourForm()
    if request.method=='POST':
        servicioForm=PlaceTourForm(request.POST, request.FILES)
        if servicioForm.is_valid():
            servicioForm.save()
        return HttpResponseRedirect('admin-servicios')
    return render(request,'admins/admin_servicios/admin_add_servicios.html',{'servicioForm':servicioForm})


@login_required(login_url='adminlogin')
def delete_servicio_view(request,pk):
    servicio=Place_Tour.objects.get(id=pk)
    servicio.delete()
    return redirect('admin-servicios')


@login_required(login_url='adminlogin')
def update_servicio_view(request,pk):
    servicio=Place_Tour.objects.get(id=pk)
    servicioForm=PlaceTourForm(instance=servicio)
    if request.method=='POST':
        servicioForm=PlaceTourForm(request.POST,request.FILES,instance=servicio)
        if servicioForm.is_valid():
            servicioForm.save()
            return redirect('admin-servicios')
    return render(request,'admins/admin_servicios/admin_update_servicio.html',{'servicioForm':servicioForm})

# admin view the feedback
@login_required(login_url='adminlogin')
def view_feedback_view(request):
    feedbacks=Feedback.objects.all().order_by('-id')
    return render(request,'admins/view_feedback.html',{'feedbacks':feedbacks})

def view_feedback_view_home(request):
    feedbacks=Feedback.objects.all().order_by('-id')
    return render(request,'webpage/home.html',{'feedbacks':feedbacks})



