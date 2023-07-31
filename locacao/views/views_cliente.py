from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from automovel.models import Automovel
from locacao.forms import FormAddLocacao
from locacao.models import Locacao


def listar_reservas(request):
    if request.user.is_authenticated:
        # Recupera as reservas feitas pelo cliente logado
        user_id = request.user.id
        reservas = Locacao.objects.filter(cliente=user_id).order_by('-data_locacao')

        context = {
            'reservas': reservas
        }
        return render(request, 'assets/static/locacao/carros_locados.html', context)

def fazer_reserva(request, carro_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        automovel = Automovel.objects.get(pk=carro_id)

        if request.method == 'POST':
            form = FormAddLocacao(request.POST)
            if form.is_valid():
                data_locacao = form.cleaned_data['data_locacao']
                data_devolucao = form.cleaned_data['data_devolucao']
                hora_locacao = form.cleaned_data['hora_locacao']
                hora_devolucao = form.cleaned_data['hora_devolucao']

                # Verifica a disponibilidade do veículo para locação
                if automovel.disponivel == False:
                    return HttpResponse('Carro não disponivel')
                else:
                    #aqui eu faço a contagem de dias atraves da data de locacao e devolucao
                    diferenca_dias = (data_devolucao - data_locacao)
                    quantidade_dias = diferenca_dias.days
                    print(quantidade_dias)
                    valor_soma = (automovel.valor_locacao * quantidade_dias)

                    # calculo da qtd de KM/dia
                    limite_km = (quantidade_dias * 100)

                    reserva = Locacao.objects.create(
                        automovel=automovel,
                        cliente_id=user_id,
                        data_locacao=data_locacao,
                        data_devolucao=data_devolucao,
                        hora_locacao=hora_locacao,
                        hora_devolucao=hora_devolucao,
                        valor_locacao=valor_soma,
                        limite_km_dia=limite_km,
                        quilometragem=0,
                        devolvido=False,

                    )
                    reserva.save()
                    #deixando o automovel indisponivel para não possibilitar algum clienta fazer a reserva dele

                    return redirect('listar_reservas')

        else:
            form = FormAddLocacao()

        locacao = Locacao.objects.filter(automovel=carro_id)
        context = {
            'form': form,
            'locacoes': locacao
        }
    else:
        return HttpResponse('faça login')

    return render(request, 'assets/static/locacao/locacao.html', context)

def cancelar_reserva(request, carro_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        carro = get_object_or_404(Automovel, pk=carro_id)

        reserva = Locacao.objects.filter(cliente=user_id, automovel=carro).first()

        if reserva.status == 'Pendente':
            reserva.status = 'Em cancelamento'
            reserva.save()

            messages.success(request, f'Pedido de cancelamento do veículo {reserva.automovel.modelo.marca.descricao} - {reserva.automovel.modelo.descricao} enviado com sucesso!')
        else:
            if reserva.devolvido == False and reserva.status == 'Retirado':
                messages.warning(request, f'Devolva o veículo {reserva.automovel.modelo.marca.descricao} - {reserva.automovel.modelo.descricao} para poder fazer o cancelamento da reserva.')
            if reserva.status == 'Em cancelamento':
                messages.warning(request, f'A Solicitação de cancelamento da reserva do veículo {reserva.automovel.modelo.marca.descricao} - {reserva.automovel.modelo.descricao} já está em andamento.')
            if reserva.status == 'Cancelado':
                messages.error(request, f'Veículo {reserva.automovel.modelo.marca.descricao} - {reserva.automovel.modelo.descricao} já se encontra cancelado')
            if reserva.status == 'Devolvido':
                messages.warning(request, f'Veículo {reserva.automovel.modelo.marca.descricao} - {reserva.automovel.modelo.descricao} já foi devolvido a locadora.')

        return redirect('listar_reservas')

    else:
        return HttpResponse('faça login')
