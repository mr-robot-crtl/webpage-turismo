from django.urls import path
from Places import views


urlpatterns = [
    path('',views.category_places, name="Places"),
    path('lug/<int:category_id>',views.placess, name="Lug"),
    path('cat',views.category_places, name="Cat"),
    path('detail-lug/<int:place_id>',views.detail_place, name="detail-lug"),

    path('place_cat_aventu',views.place_cat_aventu, name="Place_cat_aventu"),
    path('lug_cat_aventu_lug_01',views.lug_cat_aventu_lug_01, name="lug_cat_aventu_lug_01"),
    path('lug_cat_aventu_lug_02',views.lug_cat_aventu_lug_02, name="lug_cat_aventu_lug_02"),
    path('lug_cat_aventu_lug_03',views.lug_cat_aventu_lug_03, name="lug_cat_aventu_lug_03"),
    
    path('lug_cat_turismo',views.lug_cat_turismo, name="lug_cat_turismo"),
    path('lug_cat_turismo_lug_01',views.lug_cat_turismo_lug_01, name="lug_cat_turismo_lug_01"),
    path('lug_cat_turismo_lug_02',views.lug_cat_turismo_lug_02, name="lug_cat_turismo_lug_02"),
    
    path('lug_cat_comid',views.lug_cat_comid, name="lug_cat_comid"),
    path('lug_cat_comid_lug_01',views.lug_cat_comid_lug_01, name="lug_cat_comid_lug_01"),
    path('lug_cat_comid_lug_02',views.lug_cat_comid_lug_02, name="lug_cat_comid_lug_02"),
    
    path('lug_cat_seguri',views.lug_cat_seguri, name="lug_cat_seguri"),
    path('lug_cat_seguri_lug_01',views.lug_cat_seguri_lug_01, name="lug_cat_seguri_lug_01"),
    path('lug_cat_seguri_lug_02',views.lug_cat_seguri_lug_02, name="lug_cat_seguri_lug_02"),
    
    path('lug_cat_educac',views.lug_cat_educac, name="lug_cat_educac"),
    path('lug_cat_educac_lug_01',views.lug_cat_educac_lug_01, name="lug_cat_educac_lug_01"),
    path('lug_cat_educac_lug_02',views.lug_cat_educac_lug_02, name="lug_cat_educac_lug_02"),
    
    path('lug_cat_salud',views.lug_cat_salud, name="lug_cat_salud"),
    path('lug_cat_salud_lug_01',views.lug_cat_salud_lug_01, name="lug_cat_salud_lug_01"),
    path('lug_cat_salud_lug_02',views.lug_cat_salud_lug_02, name="lug_cat_salud_lug_02"),
    
    path('lug_cat_banco',views.lug_cat_banco, name="lug_cat_banco"),
    path('lug_cat_banco_lug_01',views.lug_cat_banco_lug_01, name="lug_cat_banco_lug_01"),
    path('lug_cat_banco_lug_02',views.lug_cat_banco_lug_02, name="lug_cat_banco_lug_02"),
    
    path('lug_cat_zoRecre',views.lug_cat_zoRecre, name="lug_cat_zoRecre"),
    path('lug_cat_zoRecre_lug_01',views.lug_cat_zoRecre_lug_01, name="lug_cat_zoRecre_lug_01"),
    path('lug_cat_zoRecre_lug_02',views.lug_cat_zoRecre_lug_02, name="lug_cat_zoRecre_lug_02"),
]

