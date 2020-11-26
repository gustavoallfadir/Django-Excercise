from django.shortcuts import render

from .models import Cliente, Articulo, Pedido, \
    Proveedor, Almacen, Sucursal, EmpresaAsociada

from .forms import FormularioPedido

# Create your views here.

def home_view(request):
    "Vista para el sitio principal"

    return render(request, 'home.html')


def crear_pedido_view(request):
    "Vista para la creación de pedidos"

    if request.method == 'POST':
        
        form = FormularioPedido(request.POST)
        
        if form.is_valid():
            
            form.save()

            return render(request,'pedido_creado.html')

    else:

        form = FormularioPedido(request.POST)

        context = {
            'form': form,
        }

        return render(request,'crear_pedido.html',context)


def urgentes_view(request):
    "Vista para la revisión de pedidos urgentes aún no entregados"



    pedidos_urgentes = Pedido.objects.all().filter(
        urgente=True,
        tipo_surtidor='C',
        entregado=False,
        cliente__tipo_cliente__contains="Pt")


    context = {
        'pedidos_urgentes':pedidos_urgentes,
    }

    return render(request, 'urgentes.html',context)