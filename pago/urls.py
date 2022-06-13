from django.contrib import admin
from django.urls import path
from pago import views

from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('payment-success', views.payment_success_view,name='payment-success'),

]