from django.db import models
from crm.models import Email
from crm.models import Contact

class EmailLog(models.Model):
    """ this model is used to track if the email is sent or not """

    email = models.ForeignKey(
        Email, on_delete=models.SET_NULL, null=True
    )
    contact = models.ForeignKey(
        Contact, related_name="contact_email_log", on_delete=models.SET_NULL, null=True
    )
    is_sent = models.BooleanField(default=False)
