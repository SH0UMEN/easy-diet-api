from rest_framework import serializers
from food.models import MenuScore


class MenuScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuScore
		fields = ['object', 'user', 'value']
