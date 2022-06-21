from django.contrib import admin
from .models import Guia_tour, Place_Tour, Detail_Place_Tour


# Register your models here.


class GuiaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Guia_tour, GuiaAdmin)


class PlaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Place_Tour, PlaceAdmin)

class DetailPlaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Detail_Place_Tour, DetailPlaceAdmin)

