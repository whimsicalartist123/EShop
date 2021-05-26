from django.db import models

from core.models import Address, TimeStampedModel
from users.models import CustomerModel
from product.models import Product


class OrderStatus:
    DRAFT = "draft"
    UNCONFIRMED = "unconfirmed"
    CONFIRMED = "confirmed"
    UNFULFILLED = "unfulfilled"
    FULFILLED = "fulfilled"
    CANCELLED = "cancelled"

    CHOICES = [
        (DRAFT, "Draft"),
        (UNCONFIRMED, "Unconfirmed"),
        (CONFIRMED, "Confirmed"),
        (UNFULFILLED, "Unfulfilled"),
        (FULFILLED, "Fulfilled"),
        (CANCELLED, "Cancelled"),
    ]


# Create your models here.
class Order(TimeStampedModel):
    status = models.CharField(
        max_length=32, default=OrderStatus.DRAFT, choices=OrderStatus.CHOICES
    )
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    customer = models.ForeignKey(
        CustomerModel,
        blank=True,
        null=True,
        related_name="orders",
        on_delete=models.SET_NULL
    )
    address = models.ForeignKey(
        Address, related_name="+", null=True, on_delete=models.SET_NULL
    )
    user_email = models.EmailField(blank=True, default="")
    shipping_price = models.DecimalField(
        default=0,
        decimal_places=1,
        max_digits=4,
    )

    total_order_amount = models.DecimalField(default=0, decimal_places=1, max_digits=6)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ("-pk",)

    def __str__(self):
        return f"Order - {self.id}"

    def get_customer_email(self):
        return self.customer.user.email if self.customer else self.user_email


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, related_name="line_items", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity