from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import Category
from api.serializers.category import CategorySerializer


class CategoriesView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(instance=queryset, many=True)

        return Response(serializer.data)
