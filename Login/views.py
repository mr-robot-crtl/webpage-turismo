import imp
from django.shortcuts import render,redirect,reverse
from reserva.models import Orders
from servicios.models import Detail_servicio, Servicio
from login.models import Cliente, User
from login.forms import ClienteForm, ClienteUserForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings

def cliente_signup_view(request):
    userForm=ClienteUserForm()
    clienteForm=ClienteForm()
    mydict={'userForm':userForm,'clienteForm':clienteForm}
    if request.method=='POST':
        userForm=ClienteUserForm(request.POST)
        clienteForm=ClienteForm(request.POST,request.FILES)
        if userForm.is_valid() and clienteForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            cliente=clienteForm.save(commit=False)
            cliente.user=user
            cliente.save()
            my_cliente_group = Group.objects.get_or_create(name='CLIENTE')
            my_cliente_group[0].user_set.add(user)
        return HttpResponseRedirect('clientelogin')
    return render(request,'ecom/clientesignup.html',context=mydict)

#-----------for checking user iscliente
def is_cliente(user):
    return user.groups.filter(name='CLIENTE').exists()


@login_required(login_url='clientelogin')
@user_passes_test(is_cliente)
def cliente_home_view(request):
    servicios=Servicio.objects.all()
    if 'servicio_ids' in request.COOKIES:
        servicio_ids = request.COOKIES['servicio_ids']
        counter=servicio_ids.split('|')
        servicio_count_in_cart=len(set(counter))
    else:
        servicio_count_in_cart=0
    return render(request,'ecom/index.html',{'servicios':servicios,'servicio_count_in_cart':servicio_count_in_cart})



def detail_services(request, servicio_id):
    servicios=Servicio.objects.get(id=servicio_id)
    details=Detail_servicio.objects.filter(servicio=servicios)
    return render(request, "ecom/detail_services.html",{"details":details,'servicios':servicios})









#--------------for discharge patient bill (pdf) download and printing
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

@login_required(login_url='clientelogin')
@user_passes_test(is_cliente)
def download_invoice_view(request,orderID,servicioID):
    order=Orders.objects.get(id=orderID)
    servicio=Servicio.objects.get(id=servicioID)
    mydict={
        'orderDate':order.order_date,
        'clienteName':request.user,
        'clienteEmail':order.email,
        'clienteMobile':order.mobile,
        'shipmentAddress':order.address,
        'orderStatus':order.status,

        'servicioName':servicio.name,
        'servicioImage':servicio.servicio_image,
        'servicioPrice':servicio.price,
        'servicioDescription':servicio.description,


    }
    return render_to_pdf('ecom/download_invoice.html',mydict)






@login_required(login_url='clientelogin')
@user_passes_test(is_cliente)
def my_profile_view(request):
    cliente=Cliente.objects.get(user_id=request.user.id)
    return render(request,'ecom/my_profile.html',{'cliente':cliente})


@login_required(login_url='clientelogin')
@user_passes_test(is_cliente)
def edit_profile_view(request):
    cliente=Cliente.objects.get(user_id=request.user.id)
    user=User.objects.get(id=cliente.user_id)
    userForm=ClienteUserForm(instance=user)
    clienteForm=ClienteForm(instance=cliente)
    mydict={'userForm':userForm,'clienteForm':clienteForm}
    if request.method=='POST':
        userForm=ClienteUserForm(request.POST,instance=user)
        clienteForm=ClienteForm(request.POST,instance=cliente)
        if userForm.is_valid() and clienteForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            clienteForm.save()
            return HttpResponseRedirect('my-profile')
    return render(request,'ecom/edit_profile.html',context=mydict)



#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START --------------------
#---------------------------------------------------------------------------------

