# Plantilla base Creemos Academy

Esta es la plantilla base para el proyecto en Django del tutorial de un día de Desarrollo Web.

Para poder usarla pide a tu tutor que te ayude con la instalación de Python y Django.

Cuando estes listo con el aspecto visual de tu página, copia el archivo index.html a la carpeta `pagina/templates` y el resto del archivos imagenes, css, y javascript a la carpeta `pagina/static`.

En el archivo index.html asegurate tener en la primera línea `{% load staticfiles %}`.

Cada vez que en tu archivo index tengas un enlace a un recurso de imagen, css o javascript, recuerda importarlo usando la estructura `{% static 'css/styles.css' %}` o `{% static 'js/app.js' %}` o `{% static 'img/foto.png' %}`, pidele ayuda a tu tutor para hacer esta transformación.

En el formulario recuerda añadir esta línea entre las etiquetas `<form></form>` en cualquier lugar, pero recomendamos que sea la primera línea del form `{% csrf_token %}`.

Recuerda que debes crear la base de datos antes de poder ingresar la interfaz de administrador y a tus datos.

```
python manage.py makemigrations
python manage.py migrate
```

Y por supuesto, crear tu super usuario

```
python manage.py createsuperuser
```

Recuerda que cualquier duda puedes preguntarle a cualquiera de los tutores.

Éxitos!!
