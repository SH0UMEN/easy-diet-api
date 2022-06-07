from django.db import models
from .model import Product
from food.choices import Lang


class ProductTranslation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.RESTRICT)
	title = models.TextField(max_length=200)
	language = models.CharField(max_length=2, choices=Lang.choices)
