from django.contrib import admin

from reserva.models import Orders

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

