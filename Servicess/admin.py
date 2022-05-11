from django.contrib import admin
from .models import Services

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
admin.site.register(Services,ServicioAdmin)
