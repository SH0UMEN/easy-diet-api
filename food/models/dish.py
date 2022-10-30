from django.contrib.auth.models import User
from django.db import models
from .product import Product


class Dish(models.Model):
	products = models.ManyToManyField(Product)
	title = models.CharField(max_length=30)
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to='dish_images')

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.author = request.user

		super().save_model(request, obj, form, change)
