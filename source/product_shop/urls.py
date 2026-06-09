from django.urls import path

from .views import home_page, add_new_product, add_new_category, product_detail, update_product, delete_product

urlpatterns = [
    path('', home_page, name='home_page'),
    path('products/', home_page, name='home_page'),
    path('products/<int:pk>/', product_detail, name='detail'),
    path('products/add/', add_new_product, name='add'),
    path('categories/add/', add_new_category, name='add_category'),
    path('products/<int:pk>/edit/', update_product, name='edit_product'),
    path('products/<int:pk>/delete/', delete_product, name='delete_product'),
]
