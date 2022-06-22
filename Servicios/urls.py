
from django.urls import include, path
from servicios import views

from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('servicio/afterlogin', views.afterlogin_view,name='afterlogin'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('servicio/',views.home_view,name='Servicios'),
    path('guia',views.guia_tour,name='guia'),

     
    
    
 
    path('search', views.search_view,name='search'),
    path('cliente-home', views.cliente_home_view,name='cliente-home'),

    path('detail/<int:place_tour_id>/', views.detail,name='detail'),
    path('pt', views.tour_place,name='tour'),

   
    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),

   

    path('cart', views.cart_view ,name='cart'),


    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
   
  


]
