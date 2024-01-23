from django.db import models

class Service(models.Model):
        service_name = models.CharField(max_length=200, null= True)
