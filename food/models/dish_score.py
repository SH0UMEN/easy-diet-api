from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.db import models
from .dish import Dish


class DishScore(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	object = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='scores')
	value = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
