from django.contrib import admin

from .models import Order, OrderLineItem

class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_email', 'status', 'customer', 'shipping_price', 'total_order_amount', 'paid']
    list_filter = ['paid', 'status']
    inlines = [OrderLineItemInline]

    
