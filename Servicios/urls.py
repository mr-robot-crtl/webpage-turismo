from xml.dom.minidom import Document
from django.urls import path
from Servicios import views


urlpatterns = [
    path('',views.servicio, name="Servicio"),
    path('planes/',views.planServicio, name="PlanServicio"),
    path('categoria/<int:planservicio_id>/',views.categoriaServicio, name="CategoriaServicio"),
    path('categoria-detalles/<int:categoriaservicio_id>/',views.detalleCategoria, name="DetalleCategoria"),
    

]

