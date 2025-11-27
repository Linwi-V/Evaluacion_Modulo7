from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto, Categoria, Etiqueta, Detalle
from .forms import ProductoForm, CategoriaForm, EtiquetaForm, DetalleForm

# ========== PÁGINA DE INICIO ==========
def index(request):
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    total_etiquetas = Etiqueta.objects.count()
    
    return render(request, 'productos/index.html', {
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'total_etiquetas': total_etiquetas,
    })


# ========== VISTAS DE PRODUCTOS ==========
def lista_productos(request):
    productos = Producto.objects.select_related('categoria').prefetch_related('etiquetas').all()
    return render(request, 'productos/productos/lista.html', {
        'productos': productos
    })


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/productos/detalle.html', {
        'producto': producto
    })


def crear_producto(request):
    if request.method == 'POST':
        form_producto = ProductoForm(request.POST)
        form_detalle = DetalleForm(request.POST)
        
        if form_producto.is_valid() and form_detalle.is_valid():
            producto = form_producto.save()
            detalle = form_detalle.save(commit=False)
            detalle.producto = producto
            detalle.save()
            form_producto.save_m2m()  # Guardar las etiquetas (Many-to-Many)
            
            messages.success(request, 'Producto creado exitosamente')
            return redirect('detalle_producto', id=producto.id)
    else:
        form_producto = ProductoForm()
        form_detalle = DetalleForm()
    
    return render(request, 'productos/productos/crear.html', {
        'form_producto': form_producto,
        'form_detalle': form_detalle,
        'titulo': 'Crear Producto'
    })


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    detalle = producto.detalle
    
    if request.method == 'POST':
        form_producto = ProductoForm(request.POST, instance=producto)
        form_detalle = DetalleForm(request.POST, instance=detalle)
        
        if form_producto.is_valid() and form_detalle.is_valid():
            form_producto.save()
            form_detalle.save()
            
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('detalle_producto', id=producto.id)
    else:
        form_producto = ProductoForm(instance=producto)
        form_detalle = DetalleForm(instance=detalle)
    
    return render(request, 'productos/productos/editar.html', {
        'form_producto': form_producto,
        'form_detalle': form_detalle,
        'producto': producto,
        'titulo': 'Editar Producto'
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente')
        return redirect('lista_productos')
    
    return render(request, 'productos/productos/eliminar.html', {
        'objeto': producto,
        'tipo': 'producto'
    })


# ========== VISTAS DE CATEGORÍAS ==========
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/categorias/lista.html', {
        'categorias': categorias
    })


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    
    return render(request, 'productos/categorias/formulario.html', {
        'form': form,
        'titulo': 'Crear Categoría'
    })


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'productos/categorias/formulario.html', {
        'form': form,
        'titulo': 'Editar Categoría'
    })


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente')
        return redirect('lista_categorias')
    
    return render(request, 'productos/categorias/eliminar.html', {
        'objeto': categoria,
        'tipo': 'categoría'
    })


# ========== VISTAS DE ETIQUETAS ==========
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'productos/etiquetas/lista.html', {
        'etiquetas': etiquetas
    })


def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta creada exitosamente')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    
    return render(request, 'productos/etiquetas/formulario.html', {
        'form': form,
        'titulo': 'Crear Etiqueta'
    })


def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta actualizada exitosamente')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    
    return render(request, 'productos/etiquetas/formulario.html', {
        'form': form,
        'titulo': 'Editar Etiqueta'
    })


def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        etiqueta.delete()
        messages.success(request, 'Etiqueta eliminada exitosamente')
        return redirect('lista_etiquetas')
    
    return render(request, 'productos/etiquetas/eliminar.html', {
        'objeto': etiqueta,
        'tipo': 'etiqueta'
    })