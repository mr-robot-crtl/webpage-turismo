from django.contrib import admin
from django.urls import path
from admins import views

from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),
    path('adminclick', views.adminclick_view),
    
     path('view-user', views.view_user_view,name='view-user'),
    path('view-cliente', views.view_cliente_view,name='view-cliente'),
    path('delete-cliente/<int:pk>', views.delete_cliente_view,name='delete-cliente'),
    path('update-cliente/<int:pk>', views.update_cliente_view,name='update-cliente'),

    path('admin-servicios', views.admin_servicios_view,name='admin-servicios'),
    path('admin-add-servicio', views.admin_add_servicio_view,name='admin-add-servicio'),
    path('delete-servicio/<int:pk>', views.delete_servicio_view,name='delete-servicio'),
    path('update-servicio/<int:pk>', views.update_servicio_view,name='update-servicio'),

    path('admin-guias-tour', views.admin_guias_tour,name='admin-guias-tour'),
    path('admin-add-guias', views.admin_add_guia_view,name='admin-add-guias'),
    path('delete-guia/<int:pk>', views.delete_guia_view,name='delete-guia'),
    path('update-guia/<int:pk>', views.update_guia_view,name='update-guia'),

    path('admin-places', views.admin_places,name='admin-places'),
    path('admin-add-places', views.admin_add_place_view,name='admin-add-places'),
    path('delete-places/<int:pk>', views.delete_place_view ,name='delete-places'),
    path('update-places/<int:pk>', views.update_place_view ,name='update-places'),

    path('admin-detalle-places', views.admin_detalle_places,name='admin-detalle-places'),
    path('admin-add-detalle-places', views.admin_add_detalle_place_view,name='admin-add-detalle-places'),
    path('delete-detalle-places/<int:pk>', views.delete_detalle_place_view,name='delete-detalle-places'),
    path('update-detalle-places/<int:pk>', views.update_detalle_place_view,name='update-detalle-places'),


    path('admin-cat-places', views.admin_category_places,name='admin-cat-places'),
    path('admin-add-cat-places', views.admin_add_cat_place_view,name='admin-add-cat-places'),
    path('delete-cat-places/<int:pk>', views.delete_cat_place_view,name='delete-cat-places'),
    path('update-cat-places/<int:pk>', views.update_cat_place_view,name='update-cat-places'),

    path('admin-movilidad', views.admin_movilidad,name='admin-movilidad'),
    path('admin-add-movilidad', views.admin_add_movilidad_view,name='admin-add-movilidad'),
    path('delete-movilidad/<int:pk>', views.delete_movilidad_view,name='delete-movilidad'),
    path('update-movilidad/<int:pk>', views.update_movilidad_view,name='update-movilidad'),
]