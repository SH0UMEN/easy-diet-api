from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from api.serializers.user import UserSerializer
import json


@require_POST
def login_view(request):
	data = json.loads(request.body)
	user = authenticate(request, username=data['username'], password=data['password'])

	if user is None:
		return HttpResponseForbidden()

	login(request, user)

	return JsonResponse(UserSerializer(instance=user).data)


@require_POST
def logout_view(request):
	logout(request)

	return HttpResponse(status=200)