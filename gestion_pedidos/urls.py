from django.urls import path, include
from rest_framework import routers

from .views import home_view, crear_pedido_view, urgentes_view

from .viewsets import ClienteViewSet, PedidoViewSet, ArticuloViewSet, \
    ProveedorViewSet, AlmacenViewSet, SucursalViewSet, EmpresaAsociadaViewSet

# DIRECIONES DE ROUTER PARA LA API REST
router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'articulos', ArticuloViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'almacenes', AlmacenViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'empresas_asociadas', EmpresaAsociadaViewSet)



urlpatterns = [
    #DIRECCIONES WEB
    path('', home_view),
    path('home/', home_view),
    path('crear_pedido/', crear_pedido_view),
    path('urgentes/', urgentes_view),
    #DIRECCIONES API REST
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
