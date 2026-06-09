from django.shortcuts import render, redirect, get_object_or_404

from product_shop.forms import ProductForm, CategoryForm
from product_shop.models import Product, Category



def home_page(request):
    products = Product.objects.filter(remains__gte=1).order_by('category__title', 'title')
    categories = Category.objects.order_by('title')
    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context)

def add_new_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('detail', pk=product.pk)
    return render(request, 'product_form.html', {'form': form, 'title': 'Add product'})

def add_new_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request, 'add_new_category.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=product.pk)
    return render(request, 'product_form.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home_page')
    return redirect('detail', pk=pk)