from django.shortcuts import render


def inicio(request):
    contexto = {"nombre": "profe javier"}
    productos =[
        {"nombre": "producto1", "precio": 100},
        {"nombre": "producto2", "precio": 200},
        {"nombre": "producto3", "precio": 300}
    ]

    return render(request, "dispositivos/inicio.html", {
        "contexto": contexto,
        "productos": productos
    })
