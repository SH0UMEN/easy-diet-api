from django.contrib.auth.models import User
from django.db import models
from .product import Product


class Dish(models.Model):
	products = models.ManyToManyField(Product)
	title = models.CharField(max_length=30)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='dish_images')
