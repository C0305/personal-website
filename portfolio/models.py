from django.db import models
from commons import models as commons

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=80)
    my_picture = models.ImageField(upload_to='portfolio/website/', blank=True)
    description = models.CharField(max_length=120)
    about_me = models.CharField(max_length=1000)
    top_expertise = models.CharField(max_length=200)
    my_resume = models.FileField(name="My Resume", blank=True)
    secondary_image = models.ImageField(upload_to='portfolio/website/', blank=True)
    is_default = models.BooleanField(default=False)
    seo_object = models.OneToOneField('commons.SeoObject', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id}: {self.title}"



class TechnologiesStack(models.Model):
    name = models.CharField(max_length=30)
    portfolio = models.ForeignKey(Setting, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SocialNetwork(models.Model):
    SOCIAL_NETWORKS = (
        ("YT",'YoutTube'),
        ("TW",'Twitter'),
        ("GH",'GitHub'),
        ("MD",'Medium'),
        ("LI",'Medium'),
        ("EM",'E-Mail'),
    )

    url = models.CharField(max_length=150)
    type = models.CharField(max_length=2, choices=SOCIAL_NETWORKS)

class Project(models.Model):
    image = models.ImageField(upload_to='portfolio/project/', blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    text_body = models.TextField(blank=True,null=True)
    featured = models.BooleanField(default=False)
    github = models.URLField(blank=True,null=True)
    demo = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title
