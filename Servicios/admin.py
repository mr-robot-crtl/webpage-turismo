from django.contrib import admin
from .models import PlanServicio, Movilidad, CategoriaServicio, DetalleCategoria

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class MovilidadAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class DetalleCatAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(CategoriaServicio,CategoriaAdmin)
admin.site.register(DetalleCategoria,DetalleCatAdmin)
admin.site.register(PlanServicio,PlanAdmin)
admin.site.register(Movilidad,MovilidadAdmin)
