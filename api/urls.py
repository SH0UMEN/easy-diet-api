from django.urls import re_path, include
from .views import CategoriesView, ProductsView, DishesView, DishView, MenusView, \
				MenuView, login_view, logout_view, me_view

urlpatterns = [
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
