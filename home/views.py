from django.shortcuts import render, get_object_or_404
from django.views import View
from product.models import Product, Category
from orders.forms import CartAddForm


# Create your views here.

class HomeView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(is_active=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'index.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAddForm()
        return render(request, 'product.html', {'product': product, "form": form})
