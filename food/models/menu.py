from django.contrib.auth.models import User
from django.db import models
from .dish import Dish


class Menu(models.Model):
	dishes = models.ManyToManyField(Dish)
	title = models.CharField(max_length=30)
	parent = models.ForeignKey('self', on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='menu_images')
