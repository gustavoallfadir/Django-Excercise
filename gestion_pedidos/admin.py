from django.contrib import admin

from .models import Cliente, Articulo, Pedido, \
    Proveedor, Almacen, Sucursal, EmpresaAsociada


# Register your models here.

#MODELOS PRINCIPALES

class ClienteAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')
    list_display = ('nombre', 'codigo_cliente')
    


class ArticuloAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')
    list_display = ('descripcion', 'codigo_articulo','precio')


class ProveedorAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')  
    list_display = ('nombre', 'codigo_proveedor')     


class PedidoAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')
    list_display = (
        'numero_pedido',
        'articulo', 
        'cantidad',
        'urgente',
        'cliente',
        'created')
    date_hierarchy = 'created'


# PROVEEDORES DE PEDIDOS

class AlmacenAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')
    list_display = ('nombre','codigo_almacen')

class SucursalAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')
    list_display = ('nombre','codigo_sucursal')

class EmpresaAsociadaAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')
    list_display = ('nombre','codigo_empresa')


#MODELOS PRINCIPALES

admin.site.register(Cliente,ClienteAdmin)

admin.site.register(Articulo,ArticuloAdmin)

admin.site.register(Proveedor,ProveedorAdmin)

admin.site.register(Pedido,PedidoAdmin)


#PROVEEDORES DE PEDIDOS

admin.site.register(Almacen,AlmacenAdmin)

admin.site.register(Sucursal,SucursalAdmin)

admin.site.register(EmpresaAsociada, EmpresaAsociadaAdmin)

