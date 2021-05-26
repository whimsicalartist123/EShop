from django import forms

from order.models import Order

class ShippingChoices:
    FREE = 0
    REGULAR = 200

    CHOICES = [
        (FREE, 'Free Shipping'),
        (REGULAR, 'Regular Shipping')
    ]

class CheckoutForm(forms.ModelForm):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    country = forms.CharField(required=True)
    pincode = forms.CharField(max_length=6, required=True)
    shipping_choices = forms.ChoiceField(choices=ShippingChoices.CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Order
        exclude = ('status', 'customer', 'address', 'paid', 'total_order_amount', 'shipping_price')
