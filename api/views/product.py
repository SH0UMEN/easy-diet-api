from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import Product
from api.serializers.product import ProductSerializer


class ProductsView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(instance=queryset, many=True)

        return Response(serializer.data)
