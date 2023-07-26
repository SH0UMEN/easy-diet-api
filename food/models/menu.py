from django.utils import timezone
from django.db import models
from .dish import Dish
from .scorable import Scorable
from django.conf import settings


class Menu(models.Model, Scorable):
	menu_dish_relations = models.ManyToManyField(Dish, through='MenuDish', blank=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	creation_date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='menus')
	title = models.CharField(max_length=30)
