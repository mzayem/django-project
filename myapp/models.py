from django.db import models

# Create your models here.
class Product(models.Model):
	code = models.CharField(max_length = 20)
	name = models.CharField(max_length = 15)
	price = models.FloatField()
	quantity = models.IntegerField()
	description = models.TextField()
	is_available = models.BooleanField()
