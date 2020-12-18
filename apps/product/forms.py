from django import forms
from django.forms import fields

from .models import Product

class ProductCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = [
            'seller',
            'created',
            'updated',
        ]