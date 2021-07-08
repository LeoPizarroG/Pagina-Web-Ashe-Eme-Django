from django.shortcuts import render, redirect, reverse
from .models import Producto, Comentario
from .forms import ProductoForm, ComentarioForm
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, "asheeme/comentarios.html", {'comentarios':comentarios})

def index(request):
    return render(request, "asheeme/index.html")

def aboutus(request):
    return render(request, "asheeme/aboutus.html")

def contacto(request):
    return render(request, "asheeme/contacto.html")

def pan_mujer(request):
    productos = Producto.objects.all()
    #datos = {'productos':productos}
    return render(request, "asheeme/pan_mujer.html",{'productos':productos})

def pol_mujer(request):
    productos = Producto.objects.all()
    #datos = {'productos':productos}
    return render(request, "asheeme/pol_mujer.html",{'productos':productos})

def pan_hombre(request):
    productos = Producto.objects.all()
    #datos = {'productos':productos}
    return render(request, "asheeme/pan_hombre.html",{'productos':productos})

def pol_hombre(request):
    productos = Producto.objects.all()
    #datos = {'productos':productos}
    return render(request, "asheeme/pol_hombre.html",{'productos':productos})

#Creacion de Tablas HTML
def comentarios_add(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            idComentario = form.cleaned_data.get("idComentario")
            comentario = form.cleaned_data.get("comentario")
            obj = Comentario.objects.create(
                idComentario=idComentario,
                comentario=comentario
            )
            obj.save()
            return redirect(reverse('comentarios')+ "?ok")
        else:
            return redirect(reverse('comentarios')+ "?fail")
    else:
        form = ComentarioForm()
    return render(request,'asheeme/comentarios-add.html',{'form':form})

def product_new(request):         
    if request.method == 'POST':
        form = ProductoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            marca = form.cleaned_data.get("marca")
            imagen = form.cleaned_data.get("imagen")
            tipo = form.cleaned_data.get("tipo")
            obj = Producto.objects.create(
                idProducto=idProducto,
                descripcion=descripcion,
                precio=precio,
                marca=marca,
                imagen=imagen,
                tipo=tipo
            )
            obj.save()            
            return redirect(reverse('product-new')+ "?ok")
        else:
            return redirect(reverse('product-new')+ "?fail")
    else:
        form = ProductoForm()

    return render(request,'asheeme/product-new.html',{'form':form})

#Actualizacion de Datos

def product_update(request, idProducto):
    producto = Producto.objects.get(idProducto = idProducto)
    form = ProductoForm(instance = producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES,instance=producto)
        if form.is_valid():
            form.save()                
            return redirect(reverse('index')+ "?ok")
        else:
            return redirect(reverse('product-update')+ idProducto)

    return render(request,'asheeme/product-update.html',{'form':form})

#Eliminacion de Datos

def product_delete(request, idProducto):
    producto = Producto.objects.get(idProducto = idProducto)
    producto.delete()
    return redirect(to="index")