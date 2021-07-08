from django.urls import path
from django.urls import path 
from .views import *

urlpatterns = [
    path ('', index, name='index'),
    path('pan_mujer', pan_mujer, name='pan_mujer'),
    path('pol_mujer', pol_mujer, name='pol_mujer'),
    path('pan_hombre', pan_hombre, name='pan_hombre'),
    path('pol_hombre', pol_hombre, name='pol_hombre'),
    path('contacto', contacto, name='contacto'),
    path('aboutus', aboutus, name='aboutus'),
    path('product-new/', product_new , name='product-new'),
    path('comentarios/', comentarios , name='comentarios'),
    path('comentarios-add/', comentarios_add , name='comentarios-add'),
    path('product-update/<idProducto>', product_update, name='product-update'),
    path('product-delete/<idProducto>', product_delete, name='product-delete'),
]