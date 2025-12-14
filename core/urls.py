from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tienda import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'insumos', views.InsumoViewSet)
router.register(r'pedidos', views.PedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catalogo, name='catalogo'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('pedido/', views.crear_pedido, name='crear_pedido_general'),
    path('pedido/<int:producto_id>/', views.crear_pedido, name='crear_pedido'),
    path('seguimiento/', views.seguimiento, name='seguimiento_home'),
    path('seguimiento/<uuid:token>/', views.seguimiento, name='seguimiento_url'),
    path('api/', include(router.urls)),
    path('api/pedidos/filtrar/', views.filtrar_pedidos),
    path('reporte/', views.reporte, name='reporte'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)