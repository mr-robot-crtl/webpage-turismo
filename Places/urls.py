from django.urls import path
from Places import views


urlpatterns = [
    path('',views.places, name="Places"),
    path('place_cat_aventu',views.place_cat_aventu, name="Place_cat_aventu"),
    path('lug_cat_aventu_lug_01',views.lug_cat_aventu_lug_01, name="lug_cat_aventu_lug_01"),
]

