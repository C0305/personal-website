from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(decimal_places=2)
    measurement_unit = models.CharField(max_length=15)

class SoldService(models.Model):
    service = models.ForeignKey(Service)
    customer = models.ForeignKey()
    final_price = models.DecimalField(decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class SoldServiceNote(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    sold_service = models.ForeignKey(SoldService)

class ServiceNote(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    sold_service = models.ForeignKey(Service)



