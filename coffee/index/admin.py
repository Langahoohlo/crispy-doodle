from django.contrib import admin
from .models import MealMenu, BaverageMenu

class MealMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'price')
    list_per_page = 25

class BaverageMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'price')
    list_per_page = 25

admin.site.register(MealMenu, MealMenuAdmin)
admin.site.register(BaverageMenu, BaverageMenuAdmin)
