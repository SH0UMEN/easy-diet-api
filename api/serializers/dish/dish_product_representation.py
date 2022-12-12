from api.serializers.product import ProductSerializer
from rest_framework import serializers
from food.models import DishProduct


class DishProductRepresentationSerializer(serializers.ModelSerializer):
	product = ProductSerializer()

	class Meta:
		model = DishProduct
		fields = ['product', 'grams']
