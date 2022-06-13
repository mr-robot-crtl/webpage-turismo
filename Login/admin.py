from django.contrib import admin
from login.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cliente, ClienteAdmin)

# Register your models here.
