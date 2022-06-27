from rest_framework.generics import ListAPIView
from food.models import Product
from api.serializers.product import ProductSerializer


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
