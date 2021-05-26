from django.shortcuts import redirect, render
from django.views.generic import View

from cart.cart import Cart
from users.models import CustomerModel

from .forms import CheckoutForm
from .utils import create_new_order


class CheckoutView(View):
    def get(self, *args, **kwargs):
        cart = Cart(self.request)
        if not cart:
            return redirect('cart:detail')
        form = CheckoutForm()
        if self.request.user.is_authenticated:
            initial_values = {
                'user_email': self.request.user.email,

            }
            form = CheckoutForm(initial={'user_email': self.request.user.email})
        context = {
            "checkout_form": form
        }

        return render(self.request, "order/checkout.html", context)
    
    def post(self, *args, **kwargs):

        form = CheckoutForm(self.request.POST or None)
        cart = Cart(self.request)

        if form.is_valid():
            new_order, address = create_new_order(cart=cart, data=form.cleaned_data)

            if self.request.user.is_authenticated and self.request.user.is_customer:
                customer = CustomerModel.objects.get(user=self.request.user)
                new_order.customer = customer
                address.customer = customer

            new_order.save()
            address.save()
            cart.clear()
            
            return render(self.request, "order/created.html")
