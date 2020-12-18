from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'regular_price', 'sale_price', 'active', 'created_at']
    list_filter = ['active',]
    list_editable = ['regular_price', 'sale_price', 'active']