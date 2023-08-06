from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from automovel.models import Automovel
from locacao.forms import FormEditLocacao, FormAdminLocacao
from locacao.models import Locacao
from decimal import Decimal

from locacaoVeiculos.utils import group_required



@group_required(['Gerente', 'Vendedor'], "/accounts/login/") # [ 'grupo1', 'grupo2' ]
def listar_reservas_admin(request):
    reservas = Locacao.objects.all().order_by('-data_locacao')

    search_query = request.GET.get('search')
    if search_query:
        reservas = reservas.filter(
            Q(cliente__first_name=search_query) |
            Q(cliente__last_name=search_query) |
            Q(automovel__chassi__icontains=search_query)
        )

    context = {
        'reservas': reservas
    }
    return render(request, 'assets/locacao/crud/lista_reservas_admin.html', context)
@group_required(['Gerente', 'Vendedor'], "/accounts/login/") # [ 'grupo1', 'grupo2' ]
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Locacao, id=reserva_id)

    if request.method == 'POST':
        form = FormEditLocacao(request.POST, instance=reserva)
        if form.is_valid():
            # isso é para atualizar o preço de locação do veiculo caso o cliente devolver em uma data diferente
            data_locacao = form.cleaned_data['data_locacao']
            data_devolucao = form.cleaned_data['data_devolucao']
            hora_locacao = form.cleaned_data['hora_locacao']
            hora_devolucao = form.cleaned_data['hora_devolucao']

            #aqui acontece o calculo da quantidade de dias
            diferenca_dias = (data_devolucao - data_locacao)
            quantidade_dias = diferenca_dias.days

            valor_soma = (reserva.automovel.valor_locacao * quantidade_dias)

            reserva.valor_locacao = valor_soma
            reserva.hora_locacao = hora_locacao
            reserva.hora_devolucao = hora_devolucao
            # calculo da qtd de KM/dia
            limite_km = (quantidade_dias * 100)
            reserva.limite_km_dia = limite_km
            reserva.save()

            #aqui eu faço o calculo da multa caso o cliente ultrapasse o limite de KM/dia
            if reserva.quilometragem > reserva.limite_km_dia:
                diferenca_km = (reserva.quilometragem - reserva.limite_km_dia)
                multa = (diferenca_km * 0.15) #multa de 15%
                decimal = Decimal(multa)#conversão de Int para decimal

                reserva.valor_locacao = (reserva.valor_locacao + decimal)
                reserva.save()

            #aqui eu faço a alteracao dos Km do automovel quando o admin insere os Kms pecorridos pelo cliente
            reserva.automovel.quilometragem += reserva.quilometragem
            reserva.automovel.save()

            form.save()
            messages.success(request, f'Reserva do {reserva.automovel.modelo.marca.descricao} - {reserva.automovel.modelo.descricao} alterada com sucesso!')

            #isso é para atualizar a disponibilidade do automovel quando o cliente retirar ou devolve-lo
            if reserva.status == 'Devolvido' or reserva.status == 'Cencelado':
                reserva.automovel.disponivel = True
                reserva.devolvido = True
                reserva.automovel.save()
                reserva.save()
            if reserva.status == 'Retirado':
                reserva.automovel.disponivel = False
                reserva.devolvido = False
                reserva.automovel.save()
                reserva.save()

            return redirect('listar_reservas_admin')

    else:
        form = FormEditLocacao(instance=reserva)

    context = {
        'form': form,
        'reserva': reserva,
    }
    return render(request, 'assets/locacao/crud/editar_reservas.html', context)
@group_required(['Gerente'], "/accounts/login/") # [ 'grupo1', 'grupo2' ]
def remover_reserva(request, reserva_id):
    reserva = get_object_or_404(Locacao, pk=reserva_id)
    context = {
        "reserva": reserva
    }
    return render(request, "assets/locacao/crud/remover_reserva.html", context)

def confirmar_remover_reserva(request, reserva_id):
    Locacao.objects.get(pk=reserva_id).delete()

    return redirect('listar_reservas_admin')

def alugar_veiculo(request, carro_id):
    if request.user.is_authenticated:
        carro = Automovel.objects.get(id=carro_id)
        if request.method == 'POST':
            form = FormAdminLocacao(request.POST)
            if form.is_valid():
                data_locacao = form.cleaned_data['data_locacao']
                data_devolucao = form.cleaned_data['data_devolucao']
                hora_locacao = form.cleaned_data['hora_locacao']
                hora_devolucao = form.cleaned_data['hora_devolucao']
                cliente = form.cleaned_data['cliente'].id,

                cliente_id = cliente
                print(f'cliente',cliente_id)

                status = form.cleaned_data['status'],

                # aqui eu faço a contagem de dias atraves da data de locacao e devolucao
                diferenca_dias = (data_devolucao - data_locacao)
                quantidade_dias = diferenca_dias.days
                print(quantidade_dias)
                valor_soma = (carro.valor_locacao * quantidade_dias)

                # calculo da qtd de KM/dia
                limite_km = (quantidade_dias * 100)

                reserva = Locacao.objects.create(
                    automovel=carro,
                    cliente_id=cliente_id,
                    data_locacao=data_locacao,
                    data_devolucao=data_devolucao,
                    hora_locacao=hora_locacao,
                    hora_devolucao=hora_devolucao,
                    valor_locacao=valor_soma,
                    limite_km_dia=limite_km,
                    quilometragem=0,
                    devolvido=False,
                    status=status
                )
                reserva.save()
                # deixando o automovel indisponivel para não possibilitar algum clienta fazer a reserva dele
                return redirect('listar_reservas')
        else:
            form = FormAdminLocacao()

        context = {
            'form': form
        }
        return render(request, 'assets/locacao_admins/add_locacao.html', context)































