from rest_framework.generics import ListAPIView

from food.models import Category
from api.serializers.category import CategorySerializer


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
