from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from .product import Product


class Dish(models.Model):
	dish_product_relations = models.ManyToManyField(Product, through='DishProduct', blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	description_short = models.TextField(max_length=300, default='')
	description_full = models.TextField(max_length=2000, default='')
	creation_date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='dishes')
	title = models.CharField(max_length=30)
