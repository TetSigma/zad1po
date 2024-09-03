from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.exclude(slug='')
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'product_detail.html', {'product': product})