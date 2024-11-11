from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()

