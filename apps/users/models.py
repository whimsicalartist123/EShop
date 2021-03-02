from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("Email address"), max_length=254, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    is_customer = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"User - {self.email}"

class CustomerModel(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="customer",
    )
    name = models.CharField(_("User Name"), max_length=50, default="User")
    phone = models.CharField(_("Phone Number"), max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return f"Customer - {self.user.email}"


