import imp
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from login.models import Cliente
from servicios.models import Place_Tour
from reserva.models import Orders

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
            servicios=Place_Tour.objects.all().filter(id__in = servicio_id_in_cart)
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
        Orders.objects.get_or_create(cliente=cliente,place_tour=servicio,status='Pending',email=email,mobile=mobile,address=address,fecha=fecha, num_a=num_a,num_n=num_n)

    # after order placed cookies should be deleted
    response = render(request,'pago/payment_success.html')
    response.delete_cookie('servicio_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    response.delete_cookie('fecha')
    response.delete_cookie('num_a')
    response.delete_cookie('num_n')
    return response
