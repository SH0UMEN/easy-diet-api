from django.db import models
from .category import Category


class Product(models.Model):
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.RESTRICT)
	carbohydrate = models.FloatField()
	protein = models.FloatField()
	fat = models.FloatField()
	kcal = models.IntegerField()
