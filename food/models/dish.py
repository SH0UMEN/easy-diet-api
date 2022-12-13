from django.contrib.auth.models import User
from django.db import models
from .product import Product


class Dish(models.Model):
	dish_product_relations = models.ManyToManyField(Product, through='DishProduct', blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	image = models.ImageField(upload_to='static/dish_images', null=True)
	title = models.CharField(max_length=30)
