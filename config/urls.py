from django.contrib import admin
from django.urls import path
# path sirve para crear rutas en Django, es decir, para definir las URL que se pueden acceder en la aplicación.

from Libreria.views import saludos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludar/", saludos),
]  # path("nombre_ruta", vista): es una función que se utiliza para definir una ruta en Django. "nombre_ruta" es el nombre que se le asigna a la ruta, y "vista" es la función que se ejecutará cuando se acceda a esa ruta.
