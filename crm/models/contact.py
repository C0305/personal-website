import arrow
from django.db import models
from commons.models import User
from .address import Address
from commons.models import Company
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    first_name = models.CharField(_("First name"), max_length=255)
    last_name = models.CharField(_("Last name"), max_length=255)
    mail = models.EmailField(unique=True)
    phone = PhoneNumberField(null=True, unique=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField('commons.User',related_name="crm_contact_to_users")
    created_by = models.ForeignKey('commons.User', related_name="crm_contact_by_users", on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)

    company = models.ForeignKey('commons.Company', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.first_name

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

    class Meta:
        ordering = ["-created_on"]
        app_label = "crm"
