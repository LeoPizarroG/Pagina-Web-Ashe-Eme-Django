from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Tipo(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name='Id')
    nombreTipo = models.CharField(max_length=50, verbose_name="tipo")

    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'
        ordering = ["nombreTipo"]

    def __str__(self):
        return self.nombreTipo

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=10,verbose_name='Código')
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    marca = models.CharField(max_length=100,verbose_name='Marca')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
            verbose_name = 'producto'
            verbose_name_plural = 'productos'
            ordering = ["descripcion"]

    def __str__(self):
            return self.descripcion

class Comentario(models.Model):
    idComentario = models.CharField(primary_key=True, max_length=10,verbose_name='Codigo')
    comentario = models.CharField(max_length=100, verbose_name='Comentario')

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'
        ordering = ["comentario"]

    def __str__(self) -> str:
        return self.comentario