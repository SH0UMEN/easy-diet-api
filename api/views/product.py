from rest_framework.generics import ListAPIView
from api.filters import I18NSearchFilter
from food.models import Product
from api.serializers.product import ProductSerializer


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [I18NSearchFilter]
    search_fields = ['i18n__title']
