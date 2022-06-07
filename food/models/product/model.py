from django.db import models
from food.models import Category


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.RESTRICT)
	carbohydrate = models.FloatField()
	protein = models.FloatField()
	fat = models.FloatField()
	kcal = models.IntegerField()
