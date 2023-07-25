from .dish_product import DishProductSerializer
from rest_framework import serializers
from food.models import Dish


class DishShortSerializer(serializers.ModelSerializer):
	dish_product_relations = DishProductSerializer(source='dishproduct_set', many=True, required=False)

	class Meta:
		model = Dish
		fields = ['id', 'title', 'image', 'dish_product_relations']
