from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime

# request: es un objeto que contiene toda la información de la solicitud realizada por el cliente
# HttpResponse("mensaje"): es una funcion que devuelve una respuesta HTTP con el mensaje especificado.


# vista con parametros: es una funcion que recibe parametros a traves de la url, ejem:
# def libros(request, nombre, autor): es una vista que recibe dos parametros, nombre y autor, a traves de la url, y dependiendo de lo que se pase en la url, se mostrara una respuesta diferente.
def libros(request):
    datos_libros = {
        "nombre": "Cien años de Soledad",
        "autor": "Gabriel García Márquez",
        "fecha_hoy": datetime.now(),
        "precio": 10,
    }
    # render(request, "ruta_template.html", datos): es una funcion que renderiza un template con los datos especificados, sirve para mostrar una pagina web con los datos que se le pasaron, y se devuelve el html renderizado , como respuesta HTTP.
    return render(request, "libros/index.html", datos_libros)


# redireccionamiento: es una funcion que redirige a otra url
def en_sistema(request):
    return redirect("/libros/")
