from django.shortcuts import render, redirect, get_object_or_404

from automovel.forms import FormAddMarca
from automovel.models import Marca
from locacaoVeiculos.utils import group_required


@group_required(['Gerente', 'Vendedor'], "/accounts/login/")
def adicionar_marca(request):
    if request.user.is_authenticated:
        marcas = Marca.objects.all()

        if request.method == 'POST':
            form = FormAddMarca(request.POST)

            if form.is_valid():
                form.save()
                return redirect('add_marca')
        else:
            form = FormAddMarca()

        context = {
            'marcas': marcas,
            'form': form,
        }

        return render(request, 'assets/carro/marca/add_marca.html'
                               '', context)
    else:
        return render(request, 'assets/error/401.html')
@group_required(['Gerente', 'Vendedor'], "/accounts/login/")
def editar_marca(request, marca_id):

    if request.user.is_authenticated:

        marca = get_object_or_404(Marca, pk=marca_id)
        if request.method == 'POST':
            form = FormAddMarca(request.POST, instance=marca)

            if form.is_valid():
                form.save()
                return redirect('add_marca')
        else:
            form = FormAddMarca(instance=marca)

        return render(request, "assets/carro/marca/edit_marca.html", {"ID": marca_id, "form": form})
@group_required(['Gerente'], "/accounts/login/")
def remover_marca(request, marca_id):
    marca = get_object_or_404(Marca, pk=marca_id)
    context = {
        "marca": marca
    }
    return render(request, "assets/carro/marca/remove_marca.html", context)

def confirmar_remocao_marca(request, marca_id):
    Marca.objects.get(pk=marca_id).delete()

    return redirect('add_marca')