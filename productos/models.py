from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    dimensiones = models.CharField(max_length=100, blank=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Detalle de {self.producto.nombre}"

    class Meta:
        verbose_name = "Detalle de Producto"
        verbose_name_plural = "Detalles de Productos"
