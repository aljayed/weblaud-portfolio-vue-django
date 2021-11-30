from django.contrib import admin
from api.models import ContactForm, Portfolio

# Register your models here.

admin.site.register([ContactForm, Portfolio])
