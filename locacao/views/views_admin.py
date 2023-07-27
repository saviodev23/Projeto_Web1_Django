from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from locacao.forms import FormEditLocacao
from locacao.models import Locacao
from decimal import Decimal

def listar_reservas_admin(request):
    reservas = Locacao.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        reservas = reservas.filter(
            Q(cliente__nome__icontains=search_query) |
            Q(automovel__chassi__icontains=search_query)
        )

    context = {
        'reservas': reservas
    }
    return render(request, 'assets/static/locacao/crud/locar_carros.html', context)

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
            reserva.save()

            #aqui eu faço o calculo da multa caso o cliente ultrapasse o limite de KM/dia
            if reserva.quilometragem > reserva.limite_km_dia:
                diferenca_km = (reserva.quilometragem - reserva.limite_km_dia)
                multa = (diferenca_km * 0.15)
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
                reserva.automovel.save()
            if reserva.status == 'Retirado':
                reserva.automovel.disponivel = False
                reserva.automovel.save()

            return redirect('listar_reservas_admin')

    else:
        form = FormEditLocacao(instance=reserva)

    context = {
        'form': form,
        'reserva': reserva,
    }
    return render(request, 'assets/static/locacao/crud/editar_reservas.html', context)

def remover_reserva(request, reserva_id):
    reserva = get_object_or_404(Locacao, pk=reserva_id)
    context = {
        "reserva": reserva
    }
    return render(request, "assets/static/locacao/crud/remover_reserva.html", context)

def confirmar_remover_reserva(request, reserva_id):
    Locacao.objects.get(pk=reserva_id).delete()

    return redirect('listar_reservas_admin')
