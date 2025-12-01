from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto, Pedido, Categoria

# CATÁLOGO
def catalogo(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    
    # 1. Filtro por Categoría
    cat_id = request.GET.get('categoria')
    if cat_id:
        productos = productos.filter(categoria_id=cat_id)
        
    # 2. Buscador
    query = request.GET.get('q')
    if query:
        productos = productos.filter(nombre__icontains=query)

    # 3. Filtro de Precios
    orden = request.GET.get('orden')
    if orden == 'menor':
        productos = productos.order_by('precio_base') # Ascendente
    elif orden == 'mayor':
        productos = productos.order_by('-precio_base') # Descendente

    return render(request, 'tienda/catalogo.html', {
        'productos': productos, 
        'categorias': categorias
    })

# DETALLE
def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'tienda/producto_detalle.html', {'producto': producto})

# CREAR PEDIDO
def crear_pedido(request, producto_id=None):
    producto_obj = None
    if producto_id:
        producto_obj = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        Pedido.objects.create(
            cliente_nombre=request.POST.get('nombre'),
            contacto=request.POST.get('contacto'),
            descripcion=request.POST.get('descripcion'),
            fecha_necesaria=request.POST.get('fecha') or None,
            producto_ref=producto_obj,
            origen='web',
            imagen_referencia=request.FILES.get('imagen')
        )
        # Redirigir al último pedido creado para mostrar su token
        ultimo_pedido = Pedido.objects.last()
        messages.success(request, f"¡Pedido recibido! Tu código es: {ultimo_pedido.token}")
        return redirect('seguimiento_url', token=ultimo_pedido.token)

    return render(request, 'tienda/crear_pedido.html', {'producto': producto_obj})

# SEGUIMIENTO
def seguimiento(request, token=None):
    pedido = None
    if request.method == 'POST':
        token = request.POST.get('token_buscado')
        return redirect('seguimiento_url', token=token)
    
    if token:
        try:
            pedido = Pedido.objects.get(token=token)
        except:
            messages.error(request, "Código no encontrado")
            
    return render(request, 'tienda/seguimiento.html', {'pedido': pedido})