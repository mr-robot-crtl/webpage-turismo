from django.urls import path
from Places import views


urlpatterns = [
    path('',views.category_places, name="Places"),
    path('lug/<int:category_id>',views.placess, name="Lug"),
    path('cat',views.category_places, name="Cat"),
    path('detail-lug/<int:place_id>',views.detail_place, name="detail-lug"),

]

