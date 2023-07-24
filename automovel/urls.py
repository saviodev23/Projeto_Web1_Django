
from django.urls import path
from.views.views_carro import ver_detalhes_carro, editar_carro, adicionar_carro, remover_carro, confirmar_remocao_carro
from.views.views_marca import adicionar_marca, editar_marca, remover_marca, confirmar_remocao_marca
from.views.views_modelo import adicionar_modelo, editar_modelo, remover_modelo, confirmar_remocao_modelo
urlpatterns = [
    #automovel
    path('detalhes/<int:carro_id>', ver_detalhes_carro, name="detalhes_automovel"),
    path('add/automovel/', adicionar_carro, name="add_carro"),
    path('edit/automovel/<int:carro_id>', editar_carro, name="editar_carro"),
    path('remove/automovel/<int:carro_id>', remover_carro, name="remover_carro"),
    path('confirmar/remocao/carro/<int:carro_id>', confirmar_remocao_carro, name="confirmar_remocao_carro"),

    #marca
    path('add/marca/', adicionar_marca, name="add_marca"),
    path('edit/marca/<int:marca_id>', editar_marca, name="editar_marca"),
    path('remove/marca/<int:marca_id>', remover_marca, name="remover_carro"),
    path('confirmar/remocao/marca/<int:marca_id>', confirmar_remocao_marca, name="confirmar_remocao_marca"),

    # #modelo
    path('add/modelo/', adicionar_modelo, name="add_modelo"),
    path('edit/modelo/<int:modelo_id>', editar_modelo, name="editar_modelo"),
    path('remove/modelo/<int:modelo_id>', remover_modelo, name="remover_modelo"),
    path('confirmar/remocao/modelo/<int:modelo_id>', confirmar_remocao_modelo, name="confirmar_remocao_modelo"),
]