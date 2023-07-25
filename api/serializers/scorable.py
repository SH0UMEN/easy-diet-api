from rest_framework.fields import SerializerMethodField, IntegerField, DecimalField, FloatField
from rest_framework import serializers
from django.db import models


class ScorableSerializer(metaclass=serializers.SerializerMetaclass):
	scores_count = IntegerField(source='get_scores_count', read_only=True)
	overall_score = FloatField(source='get_score', read_only=True)
	user_score = SerializerMethodField()

	def get_user_score(self, record):
		user = self.context['request'].user

		try:
			return record.scores.get(user_id=user.id).value
		except models.ObjectDoesNotExist:
			return 0
