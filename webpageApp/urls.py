from django.urls import path
from webpageApp import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('miniguia',views.miniguia, name="MiniGuia"),
    path('lugares',views.lugares, name="Lugares"),
    path('login',views.login, name="Login"),
]
