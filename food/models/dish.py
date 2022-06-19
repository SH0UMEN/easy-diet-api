from django.db import models
from .product import Product


class Dish(models.Model):
	products = models.ManyToManyField(Product)
	title = models.CharField(max_length=30)
	# author = models.ForeignKey()