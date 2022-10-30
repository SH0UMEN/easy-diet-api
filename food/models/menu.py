from django.contrib.auth.models import User
from django.db import models
from .dish import Dish


class Menu(models.Model):
	dishes = models.ManyToManyField(Dish)
	title = models.CharField(max_length=30)
	parent = models.ForeignKey('self', on_delete=models.CASCADE)
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to='menu_images')

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.author = request.user

		super().save_model(request, obj, form, change)
