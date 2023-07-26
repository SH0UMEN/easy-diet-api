from django.urls import re_path, path, include
from .ai.gpt import GPT
from .router import RouterWithOptionalSlash
from .views import *

websocket_urlpatterns = [
	re_path(r'api/ai/text\/?$', GPT.as_asgi())
]

router = RouterWithOptionalSlash()
router.register(r'dishes', DishesViewSet)
router.register(r'menus', MenusViewSet)

urlpatterns = [
	re_path(r'auth/registration\/?', registration_view),
	re_path(r'auth/login\/?', login_view),
	re_path(r'auth/logout\/?', logout_view),
	re_path(r'auth/verify\/?', verify_view),
	re_path(r'auth/me\/?', me_view),

	re_path(r'categories\/?$', CategoriesView.as_view()),
	re_path(r'products\/?$', ProductsView.as_view()),

	path('', include(router.urls))
]
