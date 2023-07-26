from django.core.validators import MaxValueValidator
from django.conf import settings
from django.db import models
from .dish import Dish


class DishScore(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	object = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='scores')
	value = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
