from django.db import models

from apps.users.models import CustomerModel


class SeoModel(models.Model):
    meta_title = models.CharField(max_length=60)
    meta_description = models.TextField(max_length=255)

    class Meta:
        abstract = True



class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    country = models.CharField(max_length=256, blank=True)
    customer = models.ForeignKey(
        CustomerModel,
        related_name="my_address",
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ('pk',)

    def __str__(self) -> str:
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
