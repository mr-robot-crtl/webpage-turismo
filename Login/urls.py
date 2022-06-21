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
    path('logout', LogoutView.as_view(template_name='login/logout.html'),name='logout'),

    path('servicio/clientesignup', views.cliente_signup_view),
    path('clientesignup', views.cliente_signup_view),
    path('servicio/clientelogin', LoginView.as_view(template_name='login/clientelogin.html'),name='clientelogin'),
    path('clientelogin', LoginView.as_view(template_name='login/clientelogin.html'),name='clientelogin'),


    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:servicioID>', views.download_invoice_view,name='download-invoice'),

]
