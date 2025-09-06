from django.shortcuts import render, redirect, get_object_or_404
from .models import Dispositivo
from .forms import DispositivoForm

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
    dispositivo = Dispositivo.objects.get(
        id=dispositivo_id
    )
    return render(request,
                "dispositivos/dispositivos.html",
                {"dispositivo": dispositivo}
                )


def crear_dispositivos(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm()
    return render(request, 'dispositivos/crear.html', {'fomr': form})

def editar_dispositivos(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == 'POST':
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm(instance=dispositivo)
    return render(request, 'dispositivos/editar.html',{'form': form})


def eliminar_dispositivos(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('listar_dispositivos')
    return render(request, 'dispositivos/eliminar.html', {'dispositivo': dispositivo})
    
