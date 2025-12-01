from django.shortcuts import render
from .models import Product

def index(request):
    """Ana səhifə görünüşü"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def product_detail(request, pk):
    """Məhsulun detalları səhifəsi"""
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
