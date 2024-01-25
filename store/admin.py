from django.contrib import admin
from .models import Service

#register the model
class ServiceAdmin(admin.ModelAdmin):
        list_display =('service_name', 'service_description')

admin.site.register(Service, ServiceAdmin)
 