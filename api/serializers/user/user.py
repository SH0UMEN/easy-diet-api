from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from .user_representation import UserRepresentationSerializer
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
	username = CharField(min_length=5, max_length=14)
	password = CharField(min_length=6, max_length=20)

	class Meta:
		model = get_user_model()
		fields = ['username', 'password', 'email']

	def to_representation(self, instance):
		return UserRepresentationSerializer(instance, source=self.source).data
