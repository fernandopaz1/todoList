# ToDo List

Este proyecto es un ToDo list desarrollado con Django

Para ejecutar este proyecto en tu computadora tendras que ejecutar los siguientes pasos.

`git clonehttps://github.com/fernandopaz1/todoList`

`cd todoList_Django`

### Entorno virtual

Creamos un entorno virtual y lo activamos

`python3 -m venv myvenv`

`source myenv/bin/activate`

Actualizamos el gestor de paquetes de python e instalamos los requerimientos de este proyecto.

`python3 -m pip install --upgrade pip`

` pip install -r requirements.txt`

### Variables de entorno

Debemos crear el archivo `/todo/.env` cuyo contenido debe ser

```DEBUG=True
SECRET_KEY=secret-key
DATABASE_NAME=nombreDB
DATABASE_USER=usuarioDB
DATABASE_PASSWORD=passwordDB
DATABASE_HOST=host
DATABASE_PORT=port
```

<ul>
<li>secret-key: se puede generar con ejecutando en la terminal el comando

`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

</li>

<li>nombreDB, usuarioDB y passwordDB deben ser el nombre de la base de datos que vamos a usar, el usuario que accede a ella y el password de la base. <br>
Todo esto debe estar previamente configurado antes de levantar el servidor. A continuacion un ejemplo de como configurar la base en PostgreSQL  para

```
nombreDB = django
usuarioDB = django_user
password = myPassword
```

```
CREATE TABLE django;
CREATE USER django_user;
ALTER USER django_user PASSWORD myPassword;
```

Tambien si tenemos pensados correr tests de Django podriamos hacer

`ALTER USER django_user WITH SUPERUSER`

ya que para correr tests Django debe poder crear y destruir bases de datos auxiliares.

</li>

<li>Para conectarse a la base se debe configurar el acceso a ella mediante el host:port. Por ejemplo en linux se deben agregar este host y port como permitidos archivo pg_hba.conf.
</li>
</ul>

### Levantar servidor

Para cargar los modelos en la base de datos debemos usar el comando

`python3 manage.py migrate`

Para montar el servidor usamos el comando

`python3 manage.py runserver`

Listo tu pagina deberia estar dispoible en la dirección [localhost](http://127.0.0.1:8000/)
