Sistema de gestión de pedidos
Versión de prueba para Mobilender

El Sistema de gestión de pedidos es una aplicación web creada con Python/Django.

Se encuentra configurada para trabajar dentro de un contenedor Docker.

Para inicializar la imagen del contenedor abra a terminal en el path donde se encuentren los 
archivos del proyecto.


Ejecute los siguientes comandos:

Inicializar el contenedor docker
$ sudo docker-compose up build .

Crear las migraciones de la base de datos a partir de los modelos de Django
$ sudo docker-compose run web python manage.py makemigrations

Migrar la base de datos por primera vez, esto creará la base de datos
$ sudo docker-compose run web python manage.py migrate

Crear un superusuario
$ sudo docker-compose run web python manage.py createsuperuser

Inicializar la aplicación Django una vez que las bases de datos están preparadas
$ sudo docker-compose up


La dirección por defecto en la que se ejecutará el servidor local es 0.0.0.0:8000
Estos parámetros se pueden ajustar dentro del archivo settings.py


La url para realizar solicitudes a través de la API REST es '/api/'.

A través de la url '/admin/' se puede acceder al panel de administración de Django.

A través de la url '/home/' o la raíz se puede acceder a la vista de inicio.