from rest_framework import serializers

from .models import Cliente, Articulo, Pedido, \
    Proveedor, Almacen, Sucursal, EmpresaAsociada

# Serializers define the API representation.

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    "Clase serializador API REST para el modelo Pedido"

    class Meta:
        model = Pedido
        fields = '__all__'


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    "Clase serializador API REST para el modelo Cliente"

    class Meta:
        model = Cliente
        fields = '__all__'


class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
    "Clase serializador API REST para el modelo Articulo"

    class Meta:
        model = Articulo
        fields = '__all__'


class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    "Clase serializador API REST para el modelo Proveedor"

    class Meta:
        model = Proveedor
        fields = '__all__'


class AlmacenSerializer(serializers.HyperlinkedModelSerializer):
    "Clase serializador API REST para el modelo Pedido"

    class Meta:
        model = Almacen
        fields = '__all__'

class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    "Clase serializador API REST para el modelo Pedido"

    class Meta:
        model = Sucursal
        fields = '__all__'

class EmpresaAsociadaSerializer(serializers.HyperlinkedModelSerializer):
    "Clase serializador API REST para el modelo Pedido"

    class Meta:
        model = EmpresaAsociada
        fields = '__all__'