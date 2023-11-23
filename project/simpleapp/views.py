from django.views.generic import ListView, DetailView
from .models import Product, Category
from .filters import ProductFilter
from datetime import datetime


class ProductsList(ListView):
    model = Product
    ordering = ['-price']
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.utcnow()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class CategoriesList(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'
