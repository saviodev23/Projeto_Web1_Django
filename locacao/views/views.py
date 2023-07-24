from django.shortcuts import render
from automovel.models import Automovel



def home(request):
    carros = Automovel.objects.all()

    context = {
        'carros': carros
    }
    return render(request, 'assets/static/index.html', context)







