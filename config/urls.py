from django.contrib import admin
from django.urls import path

# path sirve para crear rutas en Django, es decir, para definir las URL que se pueden acceder en la aplicación.
from Libreria.views import libros, en_sistema, detalle_libro
# url estatica: url que no cambia y no recibe parametros, ejem:
# path("ruta", vista): funcion que se usa para definir una ruta en Django y esto es una url estatica, osea que solo se accede mediante a la ruta que se pone y no se pueden pasar parametros por la url ,osea no se pueden usar variables en la ruta.

# url dinamica: url que cambia y recibe parametros,ejem:
# path("ruta/<tipo:parametro>/", vista): funcion que se usa para definir una ruta con parametros, es una url dinamica,
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("ruta",vista, name = "alias"): es una funcion que se usa para definir una ruta en Django, y el name es un alias que se le da a la ruta para poder referenciarla en otras partes del codigo, como en los templates, y asi no tener que escribir la ruta completa cada vez que se quiera usar.
    path("libros/", libros, name="libros"),
    path("libros/a_sistema/", en_sistema),
    path("libros/detalle/", detalle_libro, name="detalle_libro"),
]
