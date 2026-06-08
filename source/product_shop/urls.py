from django.urls import path

from .views import home_page, add_new_product, add_new_category, product_detail


urlpatterns = [
    path('', home_page, name='home_page'),
    path('add/', add_new_product, name='add'),
    path('add/category/', add_new_category, name='add_category'),
    path('product/<int:pk>/', product_detail, name='detail'),
]
