from django.db import models
from .menu import Menu
from .dish import Dish


class MenuDish(models.Model):
	dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	quantity = models.IntegerField()
