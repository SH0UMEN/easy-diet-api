from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from api.serializers.user import UserSerializer
from api.error import Error
import json


@require_POST
def registration_view(request):
	data = json.loads(request.body)

	username = data['username']
	password = data['password']

	is_username_valid = username and 5 <= len(username) <= 14
	is_password_valid = password and 6 <= len(password) <= 20

	if not is_password_valid or not is_username_valid:
		return HttpResponseBadRequest(Error.DataNotValid)

	try:
		user = User.objects.create_user(username=username, password=password)
	except BaseException:
		return HttpResponseBadRequest(Error.UsernameIsBusy)

	return JsonResponse(UserSerializer(instance=user).data)


@require_POST
def login_view(request):
	data = json.loads(request.body)
	user = authenticate(request, username=data['username'], password=data['password'])

	if user is None:
		return HttpResponseBadRequest(Error.UserNotFound)

	login(request, user)

	return JsonResponse(UserSerializer(instance=user).data)


@require_POST
def logout_view(request):
	logout(request)

	return HttpResponse(status=200)


@require_GET
def me_view(request):
	if not request.user.is_authenticated:
		return HttpResponse(Error.UserIsAuthenticated, status=401)

	return JsonResponse(UserSerializer(instance=request.user).data)
