from django.urls import re_path
from .ai.gpt import GPT
from .views import *

websocket_urlpatterns = [
	re_path(r'api/ai/text\/?$', GPT.as_asgi())
]

urlpatterns = [
	re_path(r'auth/registration\/?', registration_view),
	re_path(r'auth/login\/?', login_view),
	re_path(r'auth/logout\/?', logout_view),
	re_path(r'auth/me\/?', me_view),

	re_path(r'categories\/?$', CategoriesView.as_view()),
	re_path(r'products\/?$', ProductsView.as_view()),

	re_path(r'dishes\/?$', DishesView.as_view()),
	re_path(r'dishes/(?P<pk>\d+)\/?$', DishView.as_view()),

	re_path(r'menus\/?$', MenusView.as_view()),
	re_path(r'menus/(?P<pk>\d+)\/?$', MenuView.as_view()),
]
