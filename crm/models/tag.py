from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)