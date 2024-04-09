from django.contrib import admin
from apps.products.models import *
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')


# Register your models here.
