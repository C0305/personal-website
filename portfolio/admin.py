from django.contrib import admin
from portfolio import models as portfolio
from crm import models as crm

# Register your models here.

admin.site.register(portfolio.Project)
admin.site.register(portfolio.TechnologiesStack)
admin.site.register(portfolio.PortfolioSettings)
admin.site.register(portfolio.SocialNetwork)

admin.site.register(crm.Lead)