from django.http import HttpResponse

# request: es un objeto que contiene toda la información de la solicitud realizada por el cliente
# HttpResponse("mensaje"): es una funcion que devuelve una respuesta HTTP con el mensaje especificado.


# vista con parametros: es una funcion que recibe parametros a traves de la url
def libros(request, nombre=None, autor=None):
    if nombre and autor:
        return HttpResponse("soy vista de libros y autores")
    elif nombre:
        return HttpResponse("soy solo lista de libros")
    elif autor:
        return HttpResponse("soy solo lista de autores")
    else:
        return HttpResponse("soy vista sin parametros")
