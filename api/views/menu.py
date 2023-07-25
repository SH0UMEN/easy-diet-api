from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import MenuScoreSerializer
from api.serializers.menu import MenuSerializer
from api.permissions import ViewSetPermission
from api.views.scorable import Scorable
from food.models import Menu


class MenusViewSet(ModelViewSet, Scorable):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [ViewSetPermission]
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    ordering_fields = ['creation_date']
    filterset_fields = ['author']
    ordering = '-creation_date'
    search_fields = ['title']
    score_serializer = MenuScoreSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
