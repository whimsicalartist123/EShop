from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomerModel, VendorModel, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(CustomerModel)
class CustomerAdmin(ModelAdmin):
    pass

@admin.register(VendorModel)
class VendorAdmin(ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'name', 'is_customer',)
    list_filter = ('email', 'name', 'is_customer',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password',)}),
        ("Seller/Customer", {'fields': ('is_customer',)}),
        ("Permissions", {'fields': ('is_staff', 'is_active',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_customer', 'is_seller',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
