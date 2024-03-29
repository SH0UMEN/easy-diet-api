from .dish_product import DishProductSerializer
from api.serializers.user import UserSerializer
from rest_framework import serializers
from food.models import Dish, DishProduct
from ..scorable import ScorableSerializer


class DishSerializer(serializers.ModelSerializer, ScorableSerializer):
	dish_product_relations = DishProductSerializer(source='dishproduct_set', many=True, required=False)
	author = UserSerializer(required=False)

	class Meta:
		model = Dish
		fields = '__all__'

	def create(self, validated_data):
		relations = validated_data.pop('dishproduct_set', [])
		instance = super().create(validated_data)

		for relation in relations:
			DishProduct.objects.create(dish=instance, **relation)

		return instance

	def update(self, instance, validated_data):
		relations = validated_data.pop('dishproduct_set', None)
		instance = super().update(instance, validated_data)

		if relations is not None:
			DishProduct.objects.filter(dish_id=instance.id).delete()

			for relation in relations:
				DishProduct.objects.create(dish=instance, **relation)

		return instance
