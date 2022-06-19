from rest_framework import serializers
from food.models import Category, CategoryTranslation
from .translation import TranslationSerializer


class CategoryTranslationSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryTranslation
		fields = ['language', 'title']
		list_serializer_class = TranslationSerializer


class CategorySerializer(serializers.ModelSerializer):
	i18n = CategoryTranslationSerializer(many=True)

	class Meta:
		model = Category
		fields = '__all__'
