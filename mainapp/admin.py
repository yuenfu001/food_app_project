from django.contrib import admin
from .models import Customer,Food

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ['food_name','description']
admin.site.register(Food, FoodAdmin)
admin.site.register(Customer)
