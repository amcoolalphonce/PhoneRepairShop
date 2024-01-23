from django.db import models

class Service(models.Model):
        service_name = models.CharField(max_length=200, null= True)
        service_description = models.CharField(max_length=500, null= True)
        