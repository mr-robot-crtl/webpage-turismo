from django.contrib import admin
from django.urls import path
from admins import views

from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('view-feedback', views.view_feedback_view,name='view-feedback'),
    path('adminclick', views.adminclick_view),
    
    path('view-cliente', views.view_cliente_view,name='view-cliente'),
    path('delete-cliente/<int:pk>', views.delete_cliente_view,name='delete-cliente'),
    path('update-cliente/<int:pk>', views.update_cliente_view,name='update-cliente'),

    path('admin-servicios', views.admin_servicios_view,name='admin-servicios'),
    path('admin-add-servicio', views.admin_add_servicio_view,name='admin-add-servicio'),
    path('delete-servicio/<int:pk>', views.delete_servicio_view,name='delete-servicio'),
    path('update-servicio/<int:pk>', views.update_servicio_view,name='update-servicio'),
]