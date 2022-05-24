import imp
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Orders
from reserva.forms import OrderForm
from login.models import Cliente
from login.views import is_cliente
from servicios.models import Servicio

# Create your views here.
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
    clientecount=Cliente.objects.all().count()
    serviciocount=Servicio.objects.all().count()
    ordercount=Orders.objects.all().count()

    # for recent order tables
    orders=Orders.objects.all()
    ordered_servicios=[]
    ordered_bys=[]
    for order in orders:
        ordered_servicio=Servicio.objects.all().filter(id=order.servicio.id)
        ordered_by=Cliente.objects.all().filter(id = order.cliente.id)
        ordered_servicios.append(ordered_servicio)
        ordered_bys.append(ordered_by)

    mydict={
    'clientecount':clientecount,
    'serviciocount':serviciocount,
    'ordercount':ordercount,
    'data':zip(ordered_servicios,ordered_bys,orders),
    }
    return render(request,'ecom/admin_dashboard.html',context=mydict)

@login_required(login_url='clientelogin')
@user_passes_test(is_cliente)
def my_order_view(request):
    cliente=Cliente.objects.get(user_id=request.user.id)
    orders=Orders.objects.all().filter(cliente_id = cliente)
    ordered_servicios=[]
    for order in orders:
        ordered_servicio=Servicio.objects.all().filter(id=order.servicio.id)
        ordered_servicios.append(ordered_servicio)

    return render(request,'ecom/my_order.html',{'data':zip(ordered_servicios,orders)})

# for changing status of order (pending,delivered...)
@login_required(login_url='adminlogin')
def update_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    orderForm=OrderForm(instance=order)
    if request.method=='POST':
        orderForm=OrderForm(request.POST,instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect('admin-view-booking')
    return render(request,'ecom/update_order.html',{'orderForm':orderForm})

@login_required(login_url='adminlogin')
def delete_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')


@login_required(login_url='adminlogin')
def admin_view_booking_view(request):
    orders=Orders.objects.all()
    ordered_servicios=[]
    ordered_bys=[]
    for order in orders:
        ordered_servicio=Servicio.objects.all().filter(id=order.servicio.id)
        ordered_by=Cliente.objects.all().filter(id = order.cliente.id)
        ordered_servicios.append(ordered_servicio)
        ordered_bys.append(ordered_by)
    return render(request,'ecom/admin_view_booking.html',{'data':zip(ordered_servicios,ordered_bys,orders)})


