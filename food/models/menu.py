from django.contrib.auth.models import User
from django.db import models
from .dish import Dish


class Menu(models.Model):
	menu_dish_relations = models.ManyToManyField(Dish, through='MenuDish', blank=True)
	title = models.CharField(max_length=30)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	image = models.ImageField(upload_to='menus')
