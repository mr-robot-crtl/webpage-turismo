from django.contrib import admin
from .models import Category_Place, Place, Detail_Place

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category_Place, CategoryAdmin)

class PlaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Place, PlaceAdmin)


class DetailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Detail_Place, DetailAdmin)
