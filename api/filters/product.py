from django_filters import FilterSet, CharFilter
from .negation import NegationFilterMixin
from food.models import Product


class ProductFilterSet(FilterSet, NegationFilterMixin):
    id_not = CharFilter(field_name='id', method='is_not')

    class Meta:
        model = Product
        fields = []
