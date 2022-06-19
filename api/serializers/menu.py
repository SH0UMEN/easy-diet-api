from rest_framework import serializers
from food.models import Menu


class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = '__all__'
