from django.shortcuts import render, redirect, get_object_or_404
from automovel.forms import FormAddModelo
from automovel.models import Modelo
from locacaoVeiculos.utils import group_required

@group_required(['Gerente', 'Vendedor'], "/accounts/login/")
def adicionar_modelo(request):
    if request.user.is_authenticated:
        modelo = Modelo.objects.all()

        if request.method == 'POST':
            form = FormAddModelo(request.POST)

            if form.is_valid():
                form.save()
                return redirect('add_modelo')
        else:
            form = FormAddModelo()

        context = {
            'modelos': modelo,
            'form': form,
        }

        return render(request, 'assets/carro/modelo/add_modelo.html', context)
    else:
        return render(request, 'assets/error/401.html')
@group_required(['Gerente', 'Vendedor'], "/accounts/login/")
def editar_modelo(request, modelo_id):

    if request.user.is_authenticated:

        modelo = get_object_or_404(Modelo, pk=modelo_id)
        if request.method == 'POST':
            form = FormAddModelo(request.POST, instance=modelo)

            if form.is_valid():
                form.save()
                return redirect('add_modelo')
        else:
            form = FormAddModelo(instance=modelo)

        return render(request, "assets/carro/modelo/edit_modelo.html", {"ID": modelo_id, "form": form})
@group_required(['Gerente'], "/accounts/login/")
def remover_modelo(request, modelo_id):
    modelo = get_object_or_404(Modelo, pk=modelo_id)
    context = {
        "modelos": modelo
    }
    return render(request, "assets/carro/modelo/remove_modelo.html", context)

def confirmar_remocao_modelo(request, modelo_id):
    Modelo.objects.get(pk=modelo_id).delete()

    return redirect('add_modelo')