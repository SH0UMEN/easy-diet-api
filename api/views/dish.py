from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import Dish
from api.serializers.dish import DishSerializer


class DishesView(APIView):
    def get(self, request):
        queryset = Dish.objects.all()
        serializer = DishSerializer(instance=queryset, many=True)

        return Response(serializer.data)
