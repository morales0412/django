from django.http import HttpResponse


def saludos(
    request,
):  # request: es un objeto que contiene toda la información de la solicitud realizada por el cliente
    return HttpResponse(
        "Holaaa"
    )  # HttpResponse("mensaje"): es una funcion que devuelve una respuesta HTTP con el mensaje especificado.
