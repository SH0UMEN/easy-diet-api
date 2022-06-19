from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import Menu
from api.serializers.menu import MenuSerializer


class MenusView(APIView):
    def get(self, request):
        queryset = Menu.objects.all()
        serializer = MenuSerializer(instance=queryset, many=True)

        return Response(serializer.data)
