from django.db import models


class Lang(models.TextChoices):
	EN = 'en'
	RU = 'ru'
