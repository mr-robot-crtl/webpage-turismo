from unicodedata import name
from django.urls import path
from webpage import views
#importando settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Home"),
    path('about-pucallpa',views.about_pucallpa, name="about-pucallpa")
]
#para ver las img en el admin django
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)