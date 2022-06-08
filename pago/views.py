import imp
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from pago.forms import AddressForm
from login.models import Cliente
from servicios.models import Servicio
from reserva.models import Orders

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
                    servicios=Servicio.objects.all().filter(id__in = servicio_id_in_cart)
                    for p in servicios:
                        #total=(total+p.price)
                        total=(num_a*p.price)+(num_n*p.price)

            response = render(request, 'ecom/payment.html',{'total':total})
            response.set_cookie('email',email)
            response.set_cookie('mobile',mobile)
            response.set_cookie('address',address)
            response.set_cookie('fecha',fecha)
            response.set_cookie('num_a',num_a)
            response.set_cookie('num_b',num_n)
            return response
    return render(request,'ecom/cliente_address.html',{'addressForm':addressForm,'servicio_in_cart':servicio_in_cart,'servicio_count_in_cart':servicio_count_in_cart})









# Create your views here.
# here we are just directing to this view...actually we have to check whther payment is successful or not
#then only this view should be accessed
@login_required(login_url='clientelogin')
def payment_success_view(request):
    # Here we will place order | after successful payment
    # we will fetch cliente  mobile, address, Email
    # we will fetch servicio id from cookies then respective details from db
    # then we will create order objects and store in db
    # after that we will delete cookies because after order placed...cart should be empty
    cliente=Cliente.objects.get(user_id=request.user.id)
    servicios=None
    email=None
    mobile=None
    address=None
    fecha=None
    num_a=None
    num_n=None
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        if servicio_ids != "":
            servicio_id_in_cart=servicio_ids.split('|')
            servicios=Servicio.objects.all().filter(id__in = servicio_id_in_cart)
            # Here we get servicios list that will be ordered by one cliente at a time

    # these things can be change so accessing at the time of order...
    if 'email' in request.COOKIES:
        email=request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile=request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address=request.COOKIES['address']
    if 'fecha' in request.COOKIES:
        fecha=request.COOKIES['fecha']
    if 'num_a' in request.COOKIES:
        num_a=request.COOKIES['num_a']
    if 'num_n' in request.COOKIES:
        num_n=request.COOKIES['num_n']

    # here we are placing number of orders as much there is a servicios
    # suppose if we have 5 items in cart and we place order....so 5 rows will be created in orders table
    # there will be lot of redundant data in orders table...but its become more complicated if we normalize it
    for servicio in servicios:
        Orders.objects.get_or_create(cliente=cliente,servicio=servicio,status='Pending',email=email,mobile=mobile,address=address,fecha=fecha, num_a=num_a,num_n=num_n)

    # after order placed cookies should be deleted
    response = render(request,'ecom/payment_success.html')
    response.delete_cookie('servicio_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    response.delete_cookie('fecha')
    response.delete_cookie('num_a')
    response.delete_cookie('num_n')
    return response
