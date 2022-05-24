from django.contrib import admin
from .models import Servicio,Feedback
from login.models import Cliente
from reserva.models import Orders
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cliente, ClienteAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Servicio, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
