from django.urls import path

from .views import home_page, add_new_product, add_new_category, product_detail


urlpatterns = [
    path('products/', home_page, name='home_page'),
    path('products/<int:pk>/', product_detail, name='detail'),
    path('products/add/', add_new_product, name='add'),
    path('categories/add/', add_new_category, name='add_category'),
]
