from rest_framework import viewsets

from .models import Cliente, Articulo, Pedido, \
    Proveedor, Almacen, Sucursal, EmpresaAsociada

from . serializers import PedidoSerializer, ClienteSerializer, \
    ArticuloSerializer, ProveedorSerializer, AlmacenSerializer, \
    SucursalSerializer, EmpresaAsociadaSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    "ViewSet para la API REST del modelo Pedido"

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    "ViewSet para la API REST del modelo Cliente"

    queryset = Cliente.objects.all()
    serializer_class =  ClienteSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    "ViewSet para la API REST del modelo Articulo"

    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    "ViewSet para la API REST del modelo Proveedor"

    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class AlmacenViewSet(viewsets.ModelViewSet):
    "ViewSet para la API REST del modelo Almacen"

    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    "ViewSet para la API REST del modelo Sucursal"

    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class EmpresaAsociadaViewSet(viewsets.ModelViewSet):
    "ViewSet para la API REST del modelo EmpresaAsociada"

    queryset = EmpresaAsociada.objects.all()
    serializer_class = EmpresaAsociadaSerializer