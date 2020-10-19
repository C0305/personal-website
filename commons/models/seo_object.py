from django.db import models

class SeoObject(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    keywords = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='portfolio/website/')





