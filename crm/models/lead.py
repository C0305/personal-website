from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=80)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.id}.- {self.name} - {self.email}: {self.subject}"

    class Meta:
        app_label = "crm"
