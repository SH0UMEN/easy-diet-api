from rest_framework import serializers
from food.models import Product, ProductTranslation
from .translation import TranslationSerializer


class ProductTranslationSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductTranslation
		fields = ['language', 'title']
		list_serializer_class = TranslationSerializer


class ProductSerializer(serializers.ModelSerializer):
	i18n = ProductTranslationSerializer(many=True)

	class Meta:
		model = Product
		fields = '__all__'
