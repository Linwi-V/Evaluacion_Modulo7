from django.contrib import admin
from .models import Producto, Categoria, Etiqueta, Detalle

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(Detalle)

