from django.contrib import admin
from .models import CustomerAccount, ServiceRequest

# Register your models here.
admin.site.register([CustomerAccount, ServiceRequest])
