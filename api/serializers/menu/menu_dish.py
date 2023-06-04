from .menu_dish_representation import MenuDishRepresentationSerializer
from rest_framework import serializers
from food.models import MenuDish


class MenuDishSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuDish
		fields = ['dish', 'quantity']

	def to_representation(self, instance):
		return MenuDishRepresentationSerializer(instance, source=self.source).data
