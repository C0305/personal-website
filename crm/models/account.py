import arrow
from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from cobosio.constants import INDCHOICES, COUNTRIES
from cobosio.models import User
from crm.models import Tag
from cobosio.models import Company
from cobosio.utils import append_str_to

class Account(models.Model):

    ACCOUNT_STATUS_CHOICE = (("open", "Open"), ("close", "Close"))

    name = models.CharField(pgettext_lazy("Name of Account", "Name"), max_length=64)
    email = models.EmailField()
    phone = PhoneNumberField(null=True)
    industry = models.CharField(
        _("Industry Type"), max_length=255, choices=INDCHOICES, blank=True, null=True
    )
    # billing_address = models.ForeignKey(
    #     Address, related_name='account_billing_address', on_delete=models.CASCADE, blank=True, null=True)
    # shipping_address = models.ForeignKey(
    #     Address, related_name='account_shipping_address', on_delete=models.CASCADE, blank=True, null=True)
    billing_address_line = models.CharField(
        _("Address"), max_length=255, blank=True, null=True
    )
    billing_street = models.CharField(_("Street"), max_length=55, blank=True, null=True)
    billing_city = models.CharField(_("City"), max_length=255, blank=True, null=True)
    billing_state = models.CharField(_("State"), max_length=255, blank=True, null=True)
    billing_postcode = models.CharField(
        _("Post/Zip-code"), max_length=64, blank=True, null=True
    )
    billing_country = models.CharField(
        max_length=3, choices=COUNTRIES, blank=True, null=True
    )
    website = models.URLField(_("Website"), blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name="account_created_by", on_delete=models.SET_NULL, null=True
    )
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(
        choices=ACCOUNT_STATUS_CHOICE, max_length=64, default="open"
    )
    lead = models.ForeignKey(
        "leads.Lead", related_name="account_leads", on_delete=models.SET_NULL, null=True
    )
    contact_name = models.CharField(
        pgettext_lazy("Name of Contact", "Contact Name"), max_length=120
    )
    contacts = models.ManyToManyField(
        "contacts.Contact", related_name="account_contacts"
    )
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_on"]

    def get_complete_address(self):
        """Concatenates complete address."""
        address = ""
        add_to_address = [
            self.billing_street,
            self.billing_city,
            self.billing_state,
            self.billing_postcode,
            self.get_billing_country_display(),
        ]
        address = append_str_to(address, *add_to_address)

        return address

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

    @property
    def contact_values(self):
        contacts = list(self.contacts.values_list("id", flat=True))
        return ",".join(str(contact) for contact in contacts)

