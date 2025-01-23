from django.db import models

# Create your models here.
class BusCoordinates(models.Model):
    id = models.AutoField
    latitude = models.FloatField(default=0.0, null=True, blank=True,)
    longitude = models.FloatField(default=0.0, null=True, blank=True)
    accuracy = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"