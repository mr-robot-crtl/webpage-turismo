from django.urls import path
from Tours import views


# EXAMPLE: tourd_dia ES LO QUE VA IR EN LA BARRA DEL BUSCADOR DE URL, IMPORTAS LA FUNCION tour_dia QUE FUE CREADO EN EL FILE view.py. EL name ES CON LO QUE VAS A IDENTIDIFICAR A UNA URLS PARA POSTERIORMENTE LLAMARLE DESDE CUALQUIER FILE.
urlpatterns = [
    path('tour_dia',views.tour_dia, name="Tour_dia"),
]
