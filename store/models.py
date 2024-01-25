from django.db import models

class Service(models.Model):
        service_name = models.CharField(max_length=200, default = "Service")
        service_description = models.CharField(max_length=500, default = "Description")
        service_image = models.URLField(default = "https://images.pexels.com/photos/788946/pexels-photo-788946.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

        def __str__(self):
                return self.service_name