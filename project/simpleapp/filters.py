from django_filters import FilterSet
from .models import Product


# создаём фильтр
class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ('name', 'price', 'quantity',
                  'category')
