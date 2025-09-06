from django.contrib import admin
from django.urls import path


from dispositivos.views import inicio, dispositivos, crear_dispositivos, editar_dispositivos, eliminar_dispositivos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('dispositivos/', dispositivos, name="listar_dispositivos"),
    path('dispositivos/<int:dispositivo_id>/', dispositivos, name="dispositivo"),
    path('dispositivos/crear/', crear_dispositivos, name="crear_dispositivo"),

    path('dispositivos/eliminar/<int:dispositivo_id>/', eliminar_dispositivos, name="eliminar_dispositivo"),
    path('dispositivos/editar/<int:dispositivo_id>/', editar_dispositivos, name="editar_dispositivo"),
]