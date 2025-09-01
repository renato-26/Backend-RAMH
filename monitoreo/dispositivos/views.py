from django.shortcuts import render
from .models import dispositivos
from .forms import dispositivosForm

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

def dispositivos(request, dispositivo_id):
    dispositivo = dispositivos.objects.get(
        id=dispositivo_id
    )
    return render(request,
                "dispostivos/dispositivos.html",
                {"dispositivo": dispositivo}
                )
