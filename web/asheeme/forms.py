from django import forms
from django.forms import ModelForm
from .models import Producto, Tipo

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto

        fields = [
            'idProducto',
            'descripcion',
            'precio',
            'marca',
            'imagen',
            'tipo'
        ]        
        
        labels = {
            'idProducto':'Código Producto',
            'descripcion':'Descripción',
            'precio':'Precio Unitario $',
            'marca':'Stock',
            'imagen':"Imagen",
            'tipo':'Tipo'
        }
        widgets = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'precio':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'marca':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'})
        }


        