from django.urls import path
from .views import ProductsList, ProductDetail, CategoriesList, CategoryDetail


urlpatterns = [
    path('products/', ProductsList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('categories/', CategoriesList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
]
