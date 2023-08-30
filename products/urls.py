from django.urls import path
from .views import index, CategoryCreateView, CategoryListView, SubCategoryCreateView


app_name = 'products'
urlpatterns = [
    path('', index, name='index'),
    path('category-form/', CategoryCreateView.as_view(), name='category-form'),
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('subcategory-form/', SubCategoryCreateView.as_view(), name='subcategory-list'),
]