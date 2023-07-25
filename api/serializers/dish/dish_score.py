from rest_framework import serializers
from food.models import DishScore


class DishScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = DishScore
		fields = ['object', 'user', 'value']
