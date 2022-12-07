from rest_framework import serializers
from food.models import DishProduct
from .product import ProductSerializer


class DishProductSerializer(serializers.ModelSerializer):
	product = ProductSerializer()

	class Meta:
		model = DishProduct
		fields = ['product', 'grams']
