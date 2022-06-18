from django.db import models
from food.choices import Lang


class Category(models.Model):
	pass


class CategoryTranslation(models.Model):
	category = models.ForeignKey(Category, on_delete=models.RESTRICT)
	title = models.TextField(max_length=200)
	language = models.CharField(max_length=2, choices=Lang.choices)
