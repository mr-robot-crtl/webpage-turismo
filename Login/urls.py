from django.urls import path
from .views import Registro, cerrar_sesion, logear


urlpatterns = [
    path('',Registro.as_view(), name="Autenticacion"),
    path('cerrar_sesion',cerrar_sesion, name="CerrarSesion"),
    path('logear',logear, name="Logear"),
    #path('',views.login, name="Login"),
]
 