import math

from django.db import models
from django.conf import settings
from django.urls import reverse

from django_extensions.db.models import TitleSlugDescriptionModel
from versatileimagefield.fields import VersatileImageField

from apps.core.models import TimeStampedModel

class Category(TitleSlugDescriptionModel):

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("products:product_list", args=[self.slug])

    

class Product(TitleSlugDescriptionModel, TimeStampedModel):

    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="products",
        on_delete=models.CASCADE
    )

    sku = models.CharField(max_length=50, default="SKU_NONE")
    regular_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        blank=True, 
        null=True,
    )

    stock = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='products',   
        null=True 
    )


    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        unique_together = [['seller', 'sku']]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("products:detail", args=[str(self.id)])

    @property
    def price(self):
        if self.sale_price:
            return self.sale_price
        else:
            return self.regular_price

    @property
    def discount_percent(self):
        if self.sale_price:
            return math.round(
                ((self.regular_price - self.sale_price) / self.regular_price)*100
            )
        else:
            return 0

    def get_all_images(self):
        return self.images.all()
    
    @property
    def first_image(self):
        images = self.get_all_images()
        if len(images) == 0:
            return ""
        return images[0]
    

def image_directory_path(instance, filename):
    return f"products/{instance.product.id}/{filename}"

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, 
        related_name="images",
        on_delete=models.CASCADE
    )
    order = models.IntegerField(null=True, blank=True)
    image = VersatileImageField(upload_to=image_directory_path)
    alt = models.CharField(max_length=128, blank=True)

    class Meta:
        ordering = ("order", "pk")
        app_label = "product"
