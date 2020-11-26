from django.db import models


# Create your models here.


class Cliente(models.Model):
    "Clase modelo para clientes"

    NORMAL = 'N'
    PLATA = 'P'
    ORO = 'O'
    PLATINO = 'Pt'

    TIPOS_DE_CLIENTE = [
        (NORMAL, 'Normal'),
        (PLATA, 'Plata'),
        (ORO, 'Oro'),
        (PLATINO, 'Platino'),
    ]

    nombre = models.CharField(max_length=50)
    codigo_cliente = models.AutoField(primary_key=True)
    fotografia = models.ImageField(
        blank=True,null=True, 
        upload_to='gestion_pedidos')
    direccion = models.CharField(max_length=50)
    tipo_cliente = models.CharField(
        max_length=10,
        choices=TIPOS_DE_CLIENTE,
        default=NORMAL,
        verbose_name='Tipo de cliente'
    )
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True,verbose_name='Actualizado')


    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
    
    def __str__(self):
        return self.nombre




class Almacen(models.Model):
    "Clase modelo para almacenes que surten pedidos"

    codigo_almacen = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True,verbose_name='Actualizado')
    

    class Meta:
        verbose_name='almacen'
        verbose_name_plural='almacenes'
    
    def __str__(self):
        return self.nombre 




class Sucursal(models.Model):
    "Clase modelo para sucursales que surten pedidos"

    codigo_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True,verbose_name='Actualizado')

    class Meta:
        verbose_name='sucursal'
        verbose_name_plural='sucursales'
    
    def __str__(self):       
        return self.nombre




class EmpresaAsociada(models.Model):
    "Clase modelo para empresas asociadas que surten pedidos"

    codigo_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True,verbose_name='Actualizado')

    class Meta:
        verbose_name='empresa asociada'
        verbose_name_plural='empresas asociadas'
    
    def __str__(self):
        return self.nombre 
    



class Proveedor(models.Model):
    "Clase modelo para proveedores de artículos"

    codigo_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    articulos = models.ManyToManyField('articulo', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name='proveedor'
        verbose_name_plural='proveedores'
    
    def __str__(self):
        return self.nombre    




class Articulo(models.Model):
    "Clase modelo para articulos"

    codigo_articulo = models.AutoField(primary_key=True, auto_created=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    proveedores = models.ManyToManyField('proveedor', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name='articulo'
        verbose_name_plural='articulos'
    
    def __str__(self):
        return self.descripcion




class Pedido(models.Model):
    "Clase modelo para pedidos"

    CENTRAL = 'C'
    SUCURSAL = 'S'
    ASOCIADO = 'A'

    SURTIDOR_DE_PEDIDO = [
        (CENTRAL, 'Central'),
        (SUCURSAL, 'Sucursal'),
        (ASOCIADO, 'Empresa asociada'),
    ]

    numero_pedido = models.AutoField(primary_key=True, 
        verbose_name='Número de pedido')
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE)
    articulo = models.ForeignKey(
        Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha en que se hizo el pedido')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    urgente = models.BooleanField(default=False,verbose_name='Pedido urgente')

    tipo_surtidor = models.CharField(
        verbose_name='Quién surtirá el pedido',
        help_text='Por favor seleccione a continuación el surtidor según aplique',
        max_length=12,
        choices=SURTIDOR_DE_PEDIDO,
        default=CENTRAL)  

    codigo_almacen = models.ForeignKey(
        Almacen,
        on_delete=models.CASCADE, 
        null=True,blank=True,
        )
    codigo_sucursal = models.ForeignKey(
        Sucursal, 
        on_delete=models.CASCADE,
        null=True,blank=True,
        )
    codigo_asociado = models.ForeignKey(
        EmpresaAsociada, 
        on_delete=models.CASCADE,
        null=True,blank=True,
        )

    referencia = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        help_text='Sólo para pedidos a sucursales y asociados')

    detalle = models.TextField(
        null=True,blank=True,
        verbose_name='Detalle del pedido')

    entregado = models.BooleanField(default=False)
    fecha_entrega = models.DateField(
        blank=True, null=True,
        verbose_name='Fecha de entrega')


    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'

    def __str__(self):
        return self.articulo.descripcion


