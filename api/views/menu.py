from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from food.models import Menu
from api.serializers.menu import MenuSerializer
from api.permissions import IsOwnerOrAdminOrReadOnly


class MenusView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    ordering_fields = ['creation_date']
    filterset_fields = ['author']
    ordering = '-creation_date'
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MenuView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

