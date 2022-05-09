from django.contrib import admin
from django.urls import path, include

#COLOCAR EL NOMBRE DE CADA app.urls PARA QUE FUNCIONES LAS URLS INTERNAS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Clima.urls')),
    path('', include('webpage.urls')),
    path('tours/', include('Tours.urls')),
    path('places/', include('Places.urls')),
    path('services/', include('Servicess.urls')),
    path('login/', include('Login.urls')),
]
    
