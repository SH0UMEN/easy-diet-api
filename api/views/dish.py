from rest_framework.generics import ListCreateAPIView
from food.models import Dish
from api.serializers.dish import DishSerializer


class DishesView(ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
