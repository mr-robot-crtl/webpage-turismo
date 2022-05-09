from django.urls import path
from . import views

urlpatterns = [
    path('', views.clima, name="Clima"),
    #path("result", views.result, name="result"),
    # path('social_links', views.social_links),
]
