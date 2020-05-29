from django.contrib import admin
from .models import Country,CountryArea,City,CityArea
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(CountryArea)
class CountryAreaAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(CityArea)
class CityAreaAdmin(admin.ModelAdmin):
    pass
