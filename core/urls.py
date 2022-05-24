import imp
from django.contrib import admin
from django.urls import path, include



#COLOCAR EL NOMBRE DE CADA app.urls PARA QUE FUNCIONES LAS URLS INTERNAS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('Clima.urls')),
    path('', include('webpage.urls')),
    path('', include('servicios.urls')),
    path('', include('reserva.urls')),
    path('', include('pago.urls')),
    path('', include('admins.urls')),



    path('tours/', include('Tours.urls')),
    path('places/', include('Places.urls')),


]
    
