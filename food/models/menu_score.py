from django.core.validators import MaxValueValidator
from django.conf import settings
from django.db import models
from .menu import Menu


class MenuScore(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	object = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='scores')
	value = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
