from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,user_passes_test
from webpage.models import Feedback
from reserva.models import Orders
from login.models import Cliente, User
from login.forms import ClienteForm, ClienteUserForm
from servicios.models import Place_Tour
from servicios.forms import PlaceTourForm


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

# admin view cliente table
@login_required(login_url='adminlogin')
def view_cliente_view(request):
    clientes=Cliente.objects.all()
    return render(request,'admins/view_cliente.html',{'clientes':clientes})

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
    return render(request,'admins/admin_update_cliente.html',context=mydict)

# admin view the servicio
@login_required(login_url='adminlogin')
def admin_servicios_view(request):
    servicios=Place_Tour.objects.all()
    return render(request,'admins/admin_servicios.html',{'servicios':servicios})


# admin add servicio by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_servicio_view(request):
    servicioForm=PlaceTourForm()
    if request.method=='POST':
        servicioForm=PlaceTourForm(request.POST, request.FILES)
        if servicioForm.is_valid():
            servicioForm.save()
        return HttpResponseRedirect('admin-servicios')
    return render(request,'admins/admin_add_servicios.html',{'servicioForm':servicioForm})


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
    return render(request,'admins/admin_update_servicio.html',{'servicioForm':servicioForm})

# admin view the feedback
@login_required(login_url='adminlogin')
def view_feedback_view(request):
    feedbacks=Feedback.objects.all().order_by('-id')
    return render(request,'admins/view_feedback.html',{'feedbacks':feedbacks})

