from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.db.models import ObjectDoesNotExist
from api.serializers.user import UserSerializer
from api.error import Error
from config import *
import base64


@require_POST
def registration_view(request):
	data = request.POST

	serializer = UserSerializer(data=data)
	serializer.is_valid(raise_exception=True)

	data = serializer.validated_data

	try:
		user = get_user_model().objects.create_user(username=data['username'], password=data['password'], email=data['email'], code=get_random_string(32))
	except BaseException:
		return HttpResponseBadRequest(Error.UsernameIsBusy)

	code = str(user.id) + ':' + user.code
	code = base64.b64encode(code.encode('ascii'))
	url = request.build_absolute_uri('/') + 'auth/verify/' + code.decode('ascii')

	try:
		send_mail('Easy Diet registration', url, 'Easy Diet', [data['email']], fail_silently=False)
	except BaseException:
		user.delete()
		return HttpResponseBadRequest(Error.DataNotValid)

	return HttpResponse(status=200)


@require_POST
def verify_view(request):
	code = request.POST.get('code')

	if code is None:
		return HttpResponseBadRequest()

	code = base64.b64decode(code.encode('ascii')).decode('ascii')
	id, code = code.split(':')

	try:
		user = get_user_model().objects.get(id=id, code=code)
	except ObjectDoesNotExist:
		return HttpResponseBadRequest()

	user.code = None
	user.save()

	return HttpResponse(status=200)


@require_POST
def login_view(request):
	data = request.POST
	user = authenticate(request, username=data.get('username'), password=data.get('password'))

	if user is None:
		return HttpResponseBadRequest(Error.UserNotFound)
	elif user.code is not None:
		return HttpResponseBadRequest(Error.UserIsNotActive)

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
