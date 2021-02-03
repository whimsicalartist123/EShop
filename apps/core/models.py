from django.db import models



class SeoModel(models.Model):
    meta_title = models.CharField(max_length=60)
    meta_description = models.TextField(max_length=255)

    class Meta:
        abstract = True



class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True