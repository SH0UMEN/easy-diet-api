from api.serializers import DishShortSerializer
from rest_framework import serializers
from food.models import MenuDish


class MenuDishRepresentationSerializer(serializers.ModelSerializer):
	dish = DishShortSerializer()

	class Meta:
		model = MenuDish
		fields = ['dish', 'quantity']
