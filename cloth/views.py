from django.shortcuts import render
from .models import Product
from .product_form import ProductForm

def product_list(request):
    products= Product.objects.all()
    return render(request, 'cloth/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id =id)
    return render(request, 'cloth/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', id= product.id)
    else:
        form = ProductForm()
    return render(request, 'cloth/product_form.html',{'form':form})