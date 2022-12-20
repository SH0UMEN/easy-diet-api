from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from .product import Product


class Dish(models.Model):
	dish_product_relations = models.ManyToManyField(Product, through='DishProduct', blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	creation_date = models.DateTimeField(default=timezone.now)
	description = models.TextField(max_length=300, default='')
	image = models.ImageField(upload_to='dishes')
	title = models.CharField(max_length=30)
