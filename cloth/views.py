from django.shortcuts import render
from .models import Product

def product_list(request):
    products= Product.objects.all()
    return render(request, 'cloth/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id =id)
    return render(request, 'cloth/product_detail.html', {'product': product})
