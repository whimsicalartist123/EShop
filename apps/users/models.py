from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("Email address"), max_length=254, unique=True)
    name = models.CharField(_("User Name"), max_length=50)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    is_customer = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self) -> str:
        if self.name:
            return f"{self.name} - {self.email}"
        else:
            return f"User - {self.email}"

class CustomerModel(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="customer",
    )
    phone = models.CharField(_("Phone Number"), max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return f"Customer - {self.user.email}"

class VendorModel(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="vendor",
    )
    gst = models.CharField(_("GST Number"), max_length=15, null=True, blank=True)

    def __str__(self) -> str:
        return f"Seller - {self.user.email}"


# @receiver(post_save, sender=CustomUser)
# def create_customer_or_seller(sender, instance, created, **kwargs):
#     if created:
#         print(instance.is_customer)
#         if instance.is_customer:
#             CustomerModel.objects.create(user=instance)
#         else:
#             VendorModel.objects.create(user=instance)

