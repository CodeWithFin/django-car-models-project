from django.contrib import admin
from .models import carBrand,carModel

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'horsepower')

admin.site.register(carBrand)
admin.site.register(carModel, CarModelAdmin)

