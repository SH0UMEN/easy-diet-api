from django.urls import re_path, include

from .views import CategoriesView, ProductsView, DishesView, DishView, MenusView, MenuView

urlpatterns = [
	re_path(r'auth\/?', include('rest_framework.urls')),

	re_path(r'categories\/?$', CategoriesView.as_view()),
	re_path(r'products\/?$', ProductsView.as_view()),

	re_path(r'dishes\/?$', DishesView.as_view()),
	re_path(r'dishes/(?P<pk>\d+)\/?$', DishView.as_view()),

	re_path(r'menus\/?$', MenusView.as_view()),
	re_path(r'menus/(?P<pk>\d+)\/?$', MenuView.as_view()),
]
