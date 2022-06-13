
from django.urls import path
from reserva import views

urlpatterns = [
    path('cliente-address', views.cliente_address_view,name='cliente-address'),
    path('my-order', views.my_order_view,name='my-order'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),
   

]
