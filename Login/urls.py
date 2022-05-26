"""

Developed By : sumit kumar
facebook : fb.com/sumit.luv
Youtube :youtube.com/lazycoders


"""
from django.contrib import admin
from django.urls import path
from login import views

from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),

    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),

    path('se/clientesignup', views.cliente_signup_view),
    path('clientesignup', views.cliente_signup_view),
    path('se/clientelogin', LoginView.as_view(template_name='ecom/clientelogin.html'),name='clientelogin'),
    path('clientelogin', LoginView.as_view(template_name='ecom/clientelogin.html'),name='clientelogin'),

    path('cliente-home', views.cliente_home_view,name='cliente-home'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),

]
