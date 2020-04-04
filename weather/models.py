from django.db import models

# Create your models here.

class city(models.Model):
    name = models.CharField(max_length=30)

# show the actual city name on the dashboard
    def __str__(self):
        return self.name

#show the plural of city as cities instead of citys
    class Meta: 
        verbose_name_plural = 'cities'