from django import forms
from .models import Category, SubCategory, Products


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'slug': 'Url-адрес',
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        # form = SubCategoryForm
        # template_name = 'products/subcatigory-form.html'
        # success_url = reverse_lazy('products:category-list')
        labels = {
            'name': 'Подкатегория',
            'category': 'Категория',
        }

        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ['created_at', 'is_available']