from contextlib import redirect_stderr

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.product.models import Product

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST or None)
    if form.is_valid():
        cart.add_product(
            product,
            qty=int(form.cleaned_data['quantity']),
            override_quantity=form.cleaned_data['override']
        )
    return redirect('cart:detail')

@require_POST
def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove_product(product)
    print(cart.cart)
    return redirect('cart:detail')
    

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'override': True
            }
        )
    return render(request, 'cart/detail.html', {'cart': cart})
