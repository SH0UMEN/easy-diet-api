from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.filters import OrderingFilter
from api.serializers.dish.dish import DishSerializer
from api.permissions import IsOwnerOrAdminOrReadOnly
from food.models import Dish


class DishesView(ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ['creation_date']
    filterset_fields = ['author']
    ordering = '-creation_date'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DishView(RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
