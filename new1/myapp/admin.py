from django.contrib import admin
from myapp.models import Menu

# Register your models here.
@admin.register(Menu)

class AdminMenu(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
