from .models import Order, OrderLineItem
from core.models import Address


def create_new_order(*, cart, data):
    address = Address.objects.create(
        address=data.get("address"),
        city=data.get("city"),
        country=data.get("country"),
        pincode=data.get("pincode"),
    )

    new_order = Order.objects.create(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        address=address,
        user_email=data.get("user_email"),
        total_order_amount=cart.get_total_price(),
        shipping_price=data.get("shipping_choices"),
    )

    # Create Order Line Items.
    for item in cart:
        OrderLineItem.objects.create(
            order=new_order,
            product=item["product"],
            price=item["price"],
            quantity=int(item["quantity"]),
        )

    return new_order, address
