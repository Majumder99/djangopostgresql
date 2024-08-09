from django.db import models

# Create your models here.
# schema of table
class Cars(models.Model):
    car_name =  models.CharField(max_length=100)
    car_version = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

    def __str__(self):
        return self.name