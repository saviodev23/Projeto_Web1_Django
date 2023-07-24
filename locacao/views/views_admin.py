from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from locacao.forms import FormEditLocacao
from locacao.models import Locacao

def listar_reservas_admin(request):
    reservas = Locacao.objects.all()
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
            print(quantidade_dias)
            valor_soma = (reserva.automovel.valor_locacao * quantidade_dias)

            reserva.valor_locacao = valor_soma
            reserva.hora_locacao = hora_locacao
            reserva.hora_devolucao = hora_devolucao
            reserva.save()

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
