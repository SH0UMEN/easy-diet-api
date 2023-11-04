from rest_framework.fields import BooleanField
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


class UserRepresentationSerializer(ModelSerializer):
	isSuperuser = BooleanField(read_only=True, source='is_superuser')

	class Meta:
		model = get_user_model()
		fields = ['id', 'username', 'isSuperuser']
