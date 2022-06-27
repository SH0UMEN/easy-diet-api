from django.urls import path
from .views import CategoriesView, ProductsView, DishesView, DishView, MenusView, MenuView

urlpatterns = [
	path('categories/', CategoriesView.as_view()),
	path('products/', ProductsView.as_view()),

	path('dishes/', DishesView.as_view()),
	path('dishes/<int:pk>/', DishView.as_view()),

	path('menus/', MenusView.as_view()),
	path('menus/<int:pk>/', MenuView.as_view()),
]
