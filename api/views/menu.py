from rest_framework.generics import ListCreateAPIView
from food.models import Menu
from api.serializers.menu import MenuSerializer


class MenusView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
