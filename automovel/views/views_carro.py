from django.shortcuts import render, redirect, get_object_or_404
from automovel.forms import FormAddAutomovel
from automovel.models import Automovel
from locacao.models import Locacao
from locacaoVeiculos.utils import group_required

def ver_detalhes_carro(request, carro_id):
    if request.user.is_authenticated:

        carro = get_object_or_404(Automovel, pk=carro_id)
        locacao = Locacao.objects.filter(automovel=carro)
        context = {
            'carros': carro,
            'locacao': locacao
        }
        return render(request, 'assets/static/carro/detalhes.html', context)
    else:
        return redirect('logi')

@group_required("admin", "/client/login/") # [ 'grupo1', 'grupo2' ]
def adicionar_carro(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FormAddAutomovel(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = FormAddAutomovel()

        return render(request, 'assets/static/carro/add_carro.html', {'form': form})
    else:
        return render(request, 'assets/static/error/401.html')

def editar_carro(request, carro_id):
    if request.user.is_authenticated:

        carro = get_object_or_404(Automovel, pk=carro_id)
        if request.method == 'POST':
            form = FormAddAutomovel(request.POST, request.FILES, instance=carro)

            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = FormAddAutomovel(instance=carro)

        return render(request, "assets/static/carro/editar.html", {"ID": carro_id, "form": form})

def remover_carro(request, carro_id):
    carro = get_object_or_404(Automovel, pk=carro_id)
    context = {
        "carro": carro
    }
    return render(request, "assets/static/carro/remove.html", context)

def confirmar_remocao_carro(request, carro_id):
    Automovel.objects.get(pk=carro_id).delete()

    return redirect('home')