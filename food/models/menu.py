from django.db import models
from .dish import Dish


class Menu(models.Model):
	dishes = models.ManyToManyField(Dish)
	title = models.CharField(max_length=30)
	# author = models.ForeignKey()