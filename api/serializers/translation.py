from rest_framework import serializers
from django.db import models


class TranslationSerializer(serializers.ListSerializer):
	def to_representation(self, data):
		iterable = data.all() if isinstance(data, models.Manager) else data
		result = {}

		for item in iterable:
			value = self.child.to_representation(item)
			value.pop('language', None)

			result[item.language] = value

		return result
