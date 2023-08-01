from django.db.models import Q
from django.shortcuts import render
from automovel.models import Automovel
from locacaoVeiculos.utils import create_groups


def home(request):
    create_groups()
    carros = Automovel.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        # Filtre os carros de acordo com o search_query
        carros = carros.filter(
            Q(modelo__descricao__icontains=search_query) |
            Q(modelo__marca__descricao__icontains=search_query)
        )

    context = {
        'carros': carros
    }
    return render(request, 'assets/static/index.html', context)

def sobre(request):
    return render(request, 'assets/static/sobre.html')