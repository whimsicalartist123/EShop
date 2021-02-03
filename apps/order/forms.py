from django import forms

from apps.order.models import Order

class ShippingChoices:
    FREE = 'Free Shipping'
    REGULAR = 'Regular'

    CHOICES = [
        (FREE, 'free'),
        (REGULAR, 'regular')
    ]

class CheckoutForm(forms.ModelForm):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    address = forms.CharField(widget=forms.Textarea, required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    country = forms.CharField(required=True)
    pincode = forms.CharField(max_length=6, required=True)

    class Meta:
        model = Order
        exclude = ('status', 'customer', 'address', 'paid', 'total_order_amount')

