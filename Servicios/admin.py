from django.contrib import admin
from .models import Servicio,Detail_servicio,Guia_tour


# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    pass
admin.site.register(Servicio, ServicioAdmin)


class DetailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Detail_servicio, DetailAdmin)


class GuiaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Guia_tour, GuiaAdmin)

