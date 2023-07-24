from django.shortcuts import render, redirect, get_object_or_404

from automovel.forms import FormAddMarca
from automovel.models import Marca


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

        return render(request, 'assets/static/carro/marca/add_marca.html', context)
    else:
        return render(request, 'assets/static/error/401.html')

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

        return render(request, "assets/static/carro/marca/edit_marca.html", {"ID": marca_id, "form": form})

def remover_marca(request, marca_id):
    marca = get_object_or_404(Marca, pk=marca_id)
    context = {
        "marca": marca
    }
    return render(request, "assets/static/carro/marca/remove_marca.html", context)
def confirmar_remocao_marca(request, marca_id):
    Marca.objects.get(pk=marca_id).delete()

    return redirect('add_marca')