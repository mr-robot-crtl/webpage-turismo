from django.urls import path
from Carro import views


app_name="carro"

urlpatterns = [
    path("agregar/<int:categoriaservicio_id>/", views.agregar, name="agregar"),
    path("eliminar/<int:categoriaservicio_id>/", views.eliminar, name="eliminar"),
    path("restar/<int:categoriaservicio_id>/", views.restar, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]
