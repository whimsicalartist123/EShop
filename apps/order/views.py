from pprint import pprint
from decimal import Decimal

from django.shortcuts import render
from django.views.generic import View

from apps.cart.cart import Cart
from apps.core.models import Address

from .models import OrderLineItem, Order
from .forms import CheckoutForm


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            "checkout_form": form
        }

        return render(self.request, "order/checkout.html", context)
    
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        cart = Cart(self.request)
        if form.is_valid():
            pprint(form.cleaned_data)
            data = form.cleaned_data

            # Create new address mdoel
            address = Address.objects.create(
                address=data.get('address'),
                city=data.get('city'),
                country=data.get('country'),
                pincode=data.get('pincode'),
            )

            new_order = Order.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                address=address,
                user_email=data.get('user_email'),
                shipping_price=data.get('shipping_price'),
                total_order_amount=cart.get_total_price()
            )
            
            # Create Order Line Items.
            for item in cart:
                print(item)

                OrderLineItem.objects.create(
                    order=new_order,
                    product=item['product'],
                    price=item['price'],
                    quantity=int(item['quantity'])
                )

            if self.request.user.is_authenticated:
                if self.request.user.is_customer:
                    new_order.customer = self.request.user
                    address.customer = self.request.user

            new_order.save()
            address.save()

            cart.clear()

            return render(self.request, "order/created.html", {"order": new_order})
