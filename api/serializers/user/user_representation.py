from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


class UserRepresentationSerializer(ModelSerializer):
	username = CharField(read_only=True)

	class Meta:
		model = get_user_model()
		fields = ['id', 'username']
