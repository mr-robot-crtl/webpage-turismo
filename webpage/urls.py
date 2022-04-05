from django.urls import path
from webpage import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('miniguia',views.miniguia, name="MiniGuia"),
    path('lugares',views.lugares, name="Lugares"),
    path('login',views.login, name="Login"),
]
