from unicodedata import name
from django.urls import path
from webpage import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('about-pucallpa',views.about_pucallpa, name="about-pucallpa")
]
