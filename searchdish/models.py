from django.db import models

# Create your models here.
class Restaurants(models.Model):
    name=models.CharField(("name"),max_length=255,null=True)
    location=models.CharField(("location"),max_length=255)
    items=models.CharField(("items"),max_length=10000)

