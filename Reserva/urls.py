from django.contrib import admin
from django.urls import path
from reserva import views

from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('my-order', views.my_order_view,name='my-order'),

    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),
   

]
