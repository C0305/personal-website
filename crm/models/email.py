from django.db import models
from.account import Account
from .contact import Contact

class Email(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    recipients = models.ManyToManyField('crm.Contact')
    message_subject = models.TextField(null=True)
    message_body = models.TextField(null=True)
    timezone = models.CharField(max_length=100, default="UTC")
    scheduled_date_time = models.DateTimeField(null=True)
    scheduled_later = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    from_email = models.EmailField()
    rendered_message_body = models.TextField(null=True)

    def __str__(self):
        return self.message_subject

    class Meta:
        app_label = "crm"
