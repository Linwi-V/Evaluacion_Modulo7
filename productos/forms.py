from django import forms
from .models import Producto, Categoria, Etiqueta, Detalle

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['dimensiones', 'peso']

