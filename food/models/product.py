from django.db import models
from food.models import Category
from food.choices import Lang


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	carbohydrate = models.FloatField()
	protein = models.FloatField()
	fat = models.FloatField()
	kcal = models.IntegerField()


class ProductTranslation(models.Model):
	product = models.ForeignKey(Product, related_name='i18n', on_delete=models.CASCADE)
	title = models.TextField(max_length=200)
	language = models.CharField(max_length=2, choices=Lang.choices)
