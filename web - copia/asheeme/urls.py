from django.urls import path
from django.urls import path 
from .views import *

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('product-new/', product_new , name='product-new'),
    path('product-update/<idProducto>', product_update, name='product-update'),
    path('product-delete/<idProducto>', product_delete, name='product-delete'),
]