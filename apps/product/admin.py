from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'regular_price', 'sale_price', 'active', 'created_at']
    list_filter = ['active',]
    list_editable = ['regular_price', 'sale_price', 'active']
    inlines = [
        ProductImageInline
    ]