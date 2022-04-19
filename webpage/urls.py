from django.urls import path
from webpage import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('tours',views.tours, name="Tours"),
    path('places',views.places, name="Places"),
    path('login',views.login, name="Login"),
]
