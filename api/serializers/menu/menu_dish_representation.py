from api.serializers import DishSerializer
from rest_framework import serializers
from food.models import MenuDish


class MenuDishRepresentationSerializer(serializers.ModelSerializer):
	dish = DishSerializer()

	class Meta:
		model = MenuDish
		fields = ['product', 'grams']
