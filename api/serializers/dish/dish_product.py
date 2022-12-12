from .dish_product_representation import DishProductRepresentationSerializer
from rest_framework import serializers
from food.models import DishProduct


class DishProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = DishProduct
		fields = ['product', 'grams']

	def to_representation(self, instance):
		return DishProductRepresentationSerializer(instance, source=self.source).data
