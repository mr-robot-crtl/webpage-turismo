from django.urls import path
from Servicess import views


urlpatterns = [
    path('',views.services, name="Services"),

]