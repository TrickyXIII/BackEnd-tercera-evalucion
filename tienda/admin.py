from django.contrib import admin
from .models import Insumo, Categoria, Producto, Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'estado', 'pago', 'origen', 'fecha_solicitud')
    list_filter = ('estado', 'pago', 'origen')
    readonly_fields = ('token',) # no se toca

admin.site.register(Insumo)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Pedido, PedidoAdmin)