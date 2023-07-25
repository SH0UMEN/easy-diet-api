from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from api.filters import I18NSearchFilter, ProductFilterSet
from api.serializers.product import ProductSerializer
from food.models import Product


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, I18NSearchFilter]
    filterset_class = ProductFilterSet
    search_fields = ['i18n__title']
