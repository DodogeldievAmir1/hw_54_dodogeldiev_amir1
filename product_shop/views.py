from django.shortcuts import render, redirect, get_object_or_404

from product_shop.models import Product, Category



def home_page(request):
    products = Product.objects.all().order_by('-date')
    context = {'products': products}
    return render(request, 'index.html', context)

def add_new_product(request):
    if request.method == 'POST':
        Product.objects.create(
            title=request.POST.get('title'),
            price=request.POST.get('price'),
            description_product=request.POST.get('description_product'),
            category_id=request.POST.get('category'),
            image=request.POST.get('image')
        )
        return redirect('home_page')

    categories = Category.objects.all()
    return render(request, 'create_new_pos_product.html', {'categories': categories})

def add_new_category(request):
    if request.method == 'POST':
        Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return redirect('home_page')