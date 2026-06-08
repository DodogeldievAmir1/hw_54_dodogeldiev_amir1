from django.shortcuts import render, redirect, get_object_or_404

from product_shop.models import Product, Category



def home_page(request):
    products = Product.objects.all().order_by('-date')
    context = {'products': products}
    return render(request, 'index.html', context)

def add_new_product(request):
    if request.method == 'POST':
        product = Product.objects.create(
            title=request.POST.get('title'),
            price=request.POST.get('price'),
            description_product=request.POST.get('description_product'),
            category_id=request.POST.get('category'),
            image=request.POST.get('image')
        )
        return redirect('detail', pk=product.pk)

    categories = Category.objects.all()
    return render(request, 'create_new_pos_product.html', {'categories': categories})

def add_new_category(request):
    if request.method == 'POST':
        Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return redirect('home_page')
    return render(request, 'add_new_category.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)