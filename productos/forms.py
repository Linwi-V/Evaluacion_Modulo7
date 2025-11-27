from django import forms
from .models import Producto, Categoria, Etiqueta, Detalle

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'etiquetas': forms.CheckboxSelectMultiple(),
        }
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['dimensiones', 'peso']
        widgets = {
            'dimensiones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10x20x5 cm'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1.5'})
        }

