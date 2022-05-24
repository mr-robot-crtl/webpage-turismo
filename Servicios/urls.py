
from django.urls import include, path
from servicios import views

from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('se/',views.home_view,name='Servicios'),
   
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),



    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),

]
