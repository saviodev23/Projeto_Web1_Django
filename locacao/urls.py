from django.urls import path
from.views.views_cliente import fazer_reserva, listar_reservas, cancelar_reserva
from.views.views import home
from.views.views_admin import listar_reservas_admin, editar_reserva, remover_reserva, confirmar_remover_reserva

urlpatterns = [
    #views
    path('', home, name="home"),
    #views cliente
    path('fazer/reserva/<int:carro_id>', fazer_reserva, name="fazer_reserva"),
    path('lista/reservas/', listar_reservas, name="listar_reservas"),
    path('cancelar/reserva/<int:carro_id>', cancelar_reserva, name="cancelar_reserva"),

    #views admin
    path('reservas/admin', listar_reservas_admin, name='listar_reservas_admin'),
    path('editar/reserva/<int:reserva_id>', editar_reserva, name='editar_reserva'),
    path('remover/reserva/<int:reserva_id>', remover_reserva, name="remover_reserva"),
    path('confirmar/remocao/reserva/<int:reserva_id>', confirmar_remover_reserva, name="confirmar_remover_reserva")
]