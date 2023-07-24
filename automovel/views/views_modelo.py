from django.shortcuts import render, redirect, get_object_or_404

from automovel.forms import FormAddModelo
from automovel.models import Modelo


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

        return render(request, 'assets/static/carro/modelo/add_modelo.html', context)
    else:
        return render(request, 'assets/static/error/401.html')

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

        return render(request, "assets/static/carro/modelo/edit_modelo.html", {"ID": modelo_id, "form": form})

def remover_modelo(request, modelo_id):
    modelo = get_object_or_404(Modelo, pk=modelo_id)
    context = {
        "modelos": modelo
    }
    return render(request, "assets/static/carro/modelo/remove_modelo.html", context)
def confirmar_remocao_modelo(request, modelo_id):
    Modelo.objects.get(pk=modelo_id).delete()

    return redirect('add_modelo')