from django.contrib import admin
from django.urls import path
from pago import views

from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [

    path('cliente-address', views.cliente_address_view,name='cliente-address'),
    path('payment-success', views.payment_success_view,name='payment-success'),

]