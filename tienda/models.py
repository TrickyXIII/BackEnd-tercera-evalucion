from django.db import models
import uuid
from django.core.exceptions import ValidationError

# GESTIÓN INTERNA (INSUMOS)
class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)
    unidad = models.CharField(max_length=20, blank=True)
    marca = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    
    def __str__(self): return f"{self.nombre} ({self.cantidad})"

# CATÁLOGO DE PRODUCTOS
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio_base = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    imagen_2 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen_3 = models.ImageField(upload_to='productos/', blank=True, null=True)
    destacado = models.BooleanField(default=False)

    def __str__(self): return self.nombre

# PEDIDOS
class Pedido(models.Model):
    
    ESTADOS = [
        ('solicitado', 'Solicitado'), ('aprobado', 'Aprobado'),
        ('proceso', 'En proceso'), ('realizada', 'Realizada'),
        ('entregada', 'Entregada'), ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]
    PAGOS = [('pendiente', 'Pendiente'), ('pagado', 'Pagado')]
    
    # Datos del cliente y pedido
    cliente_nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    producto_ref = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField()
    fecha_necesaria = models.DateField(null=True, blank=True)
    imagen_referencia = models.ImageField(upload_to='pedidos/', blank=True, null=True)
    ORIGENES = [
        ('web', 'Sitio Web'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('whatsapp', 'WhatsApp'),
        ('presencial', 'Presencial'),
    ]
    # GESTRIÓN ADMINISTRATIVA
    estado = models.CharField(max_length=20, choices=ESTADOS, default='solicitado')
    pago = models.CharField(max_length=20, choices=PAGOS, default='pendiente')
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    origen = models.CharField(max_length=20, choices=ORIGENES, default='web')
    def __str__(self): return f"Pedido {self.id} - {self.cliente_nombre}"

    # VALIDACIÓN DEL PAGO
    def clean(self):
        if self.estado in ['entregada', 'realizada'] and self.pago == 'pendiente':
            raise ValidationError('No se puede finalizar/entregar un pedido si el pago está pendiente.')

    def save(self, *args, **kwargs):
        self.full_clean() # Llama a la validación antes de guardar
        super().save(*args, **kwargs)