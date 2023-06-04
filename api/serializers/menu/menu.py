from .menu_dish import MenuDishSerializer
from api.serializers.user import UserSerializer
from rest_framework import serializers
from food.models import Menu, MenuDish


class MenuSerializer(serializers.ModelSerializer):
	dish_product_relations = MenuDishSerializer(source='menudish_set', many=True, required=False)
	author = UserSerializer(required=False)

	class Meta:
		model = Menu
		fields = '__all__'

	def create(self, validated_data):
		relations = validated_data.pop('menudish_set', [])
		instance = super().create(validated_data)

		for relation in relations:
			MenuDish.objects.create(meny=instance, **relation)

		return instance

	def update(self, instance, validated_data):
		relations = validated_data.pop('menudish_set', None)
		instance = super().update(instance, validated_data)

		if relations is not None:
			MenuDish.objects.filter(menu_id=instance.id).delete()

			for relation in relations:
				MenuDish.objects.create(menu=instance, **relation)

		return instance
