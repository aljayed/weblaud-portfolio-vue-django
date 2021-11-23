from django.contrib import admin
from basic_info.models import ContactFormModel, PortfolioModel

# Register your models here.

admin.site.register([ContactFormModel, PortfolioModel])
