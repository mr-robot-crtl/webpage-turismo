import imp
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Orders
from reserva.forms import OrderForm, AddressForm
from login.models import Cliente
from login.views import is_cliente
from servicios.models import Place_Tour

# shipment address before placing order
@login_required(login_url='clientelogin')
def cliente_address_view(request):
    # this is for checking whether servicio is present in cart or not
    # if there is no servicio in cart we will not show address form
    servicio_in_cart=False
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        if servicio_ids != "":
            servicio_in_cart=True
    #for counter in cart
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0

    addressForm = AddressForm()
    if request.method == 'POST':
        addressForm = AddressForm(request.POST)
        if addressForm.is_valid():
            # here we are taking address, email, mobile at time of order placement
            # we are not taking it from cliente account table because
            # these thing can be changes
            email = addressForm.cleaned_data['Email']
            mobile=addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']
            fecha = addressForm.cleaned_data['fecha']
            num_a = addressForm.cleaned_data['num_a']
            num_n = addressForm.cleaned_data['num_n']
            
            #for showing total price on payment page.....accessing id from cookies then fetching  price of servicio from db
            total=0

            if 'servicio_ids' in request.COOKIES:
                servicio_ids = request.COOKIES['servicio_ids']
                if servicio_ids != "":
                    servicio_id_in_cart=servicio_ids.split('|')
                    servicios=Place_Tour.objects.all().filter(id__in = servicio_id_in_cart)
                    for p in servicios:
                        #total=(total+p.price)
                        total=(num_a*p.price)+(num_n*p.price_menor)

            response = render(request, 'pago/payment.html',{'total':total})
     
            response.set_cookie('email',email)
            response.set_cookie('mobile',mobile)
            response.set_cookie('address',address)
            response.set_cookie('fecha',fecha)
            response.set_cookie('num_a',num_a)
            response.set_cookie('num_n',num_n)
            return response
    return render(request,'reserva/cliente_address.html',{'addressForm':addressForm,'servicio_in_cart':servicio_in_cart,'servicio_count_in_cart':servicio_count_in_cart})

@login_required(login_url='clientelogin')
@user_passes_test(is_cliente)
def my_order_view(request):  

    cliente=Cliente.objects.get(user_id=request.user.id)
    orders=Orders.objects.all().filter(cliente_id = cliente)
    ordered_servicios=[]
    for order in orders:
        ordered_servicio=Place_Tour.objects.all().filter(id=order.place_tour.id)
        ordered_servicios.append(ordered_servicio)

    return render(request,'reserva/my_order.html',{'data':zip(ordered_servicios,orders)})

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
    return render(request,'reserva/update_order.html',{'orderForm':orderForm})

@login_required(login_url='adminlogin')
def delete_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')





