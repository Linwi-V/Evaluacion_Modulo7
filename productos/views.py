from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Etiqueta, Detalle
from .forms import ProductoForm, CategoriaForm, EtiquetaForm, DetalleForm

# --- Página de inicio ---
def index(request):
    return render(request, 'productos/index.html')


# --- Productos ---
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/productos/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == "POST":
        producto_form = ProductoForm(request.POST)
        detalle_form = DetalleForm(request.POST)
        if producto_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save()
            detalle = detalle_form.save(commit=False)
            detalle.producto = producto
            detalle.save()
            return redirect('lista_productos')
    else:
        producto_form = ProductoForm()
        detalle_form = DetalleForm()
    
    return render(request, 'productos/productos/crear.html', {
        'producto_form': producto_form,
        'detalle_form': detalle_form
    })

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/productos/detalle.html', {'producto': producto})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/productos/editar.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/productos/eliminar.html', {'producto': producto})


# --- Categorías ---
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/categorias/lista.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'productos/categorias/formulario.html', {'form': form})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'productos/categorias/formulario.html', {'form': form})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'productos/categorias/formulario.html', {'categoria': categoria})


# --- Etiquetas ---
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'productos/etiquetas/lista.html', {'etiquetas': etiquetas})

def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'productos/etiquetas/formulario.html', {'form': form})

def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'productos/etiquetas/formulario.html', {'form': form})

def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'productos/etiquetas/formulario.html', {'etiqueta': etiqueta})
