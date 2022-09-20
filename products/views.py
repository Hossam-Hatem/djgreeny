from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Category , Brand 
# Create your views here.


class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class BrandList(ListView):
    model = Brand
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all
        return context
    

class BrandDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["product_brands"] = Product.objects.filter(brand=brand)
        return context
    
class CategoryList(ListView):
    model = Category

class CategoryDetail(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context["product_category"] = Product.objects.filter(category=category)
        return context
