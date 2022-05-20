from django.urls import path
from Places import views


urlpatterns = [
    path('',views.places, name="Places"),
    path('place_cat_aventu',views.place_cat_aventu, name="Place_cat_aventu"),
    path('lug_cat_aventu_lug_01',views.lug_cat_aventu_lug_01, name="lug_cat_aventu_lug_01"),
    path('lug_cat_aventu_lug_02',views.lug_cat_aventu_lug_02, name="lug_cat_aventu_lug_02"),
    path('lug_cat_turismo',views.lug_cat_turismo, name="lug_cat_turismo"),
    path('lug_cat_turismo_lug_01',views.lug_cat_turismo_lug_01, name="lug_cat_turismo_lug_01"),
    path('lug_cat_turismo_lug_02',views.lug_cat_turismo_lug_02, name="lug_cat_turismo_lug_02"),
]

