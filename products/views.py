from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)

def show(request, product_id):
    context = {'product': get_object_or_404(Product, pk=product_id)}
    return render(request, 'products/show.html', context)
    
