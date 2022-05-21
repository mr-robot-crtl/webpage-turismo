from django.contrib import admin
from .models import Lugares

# Register your models here.
class LugaresAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Lugares,LugaresAdmin)
