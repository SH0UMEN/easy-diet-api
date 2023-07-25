from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import DishScoreSerializer
from api.serializers.dish.dish import DishSerializer
from api.permissions import ViewSetPermission
from api.filters import DishFilterSet
from api.views.scorable import Scorable
from food.models import Dish


class DishesViewSet(ModelViewSet, Scorable):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [ViewSetPermission]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = DishFilterSet
    ordering_fields = ['creation_date']
    ordering = '-creation_date'
    search_fields = ['title']
    score_serializer = DishScoreSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
