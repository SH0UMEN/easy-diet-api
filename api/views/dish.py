from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from food.models import Dish
from api.serializers.dish.dish import DishSerializer
from api.permissions import IsOwnerOrReadOnly


class DishesView(ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['author']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DishView(RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminUser, IsOwnerOrReadOnly]
