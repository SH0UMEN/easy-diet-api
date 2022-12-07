from django.db import models
from .product import Product
from .dish import Dish


class DishProduct(models.Model):
	dish = models.ForeignKey(Dish, blank=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	grams = models.IntegerField()
