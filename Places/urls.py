from django.urls import path
from Places import views


urlpatterns = [
    path('',views.places, name="Places"),
    path('place_cat_aventu',views.place_cat_aventu, name="Place_cat_aventu"),
]

