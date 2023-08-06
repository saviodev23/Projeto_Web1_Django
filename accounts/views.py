# from django.contrib.auth import login
# from django.contrib.auth.models import Group
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from accounts.backend import CustomBackend
# from accounts.forms import CustomUserCreationForm, CustomLoginForm
# from accounts.models import User

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            group = Group.objects.get(name='Cliente')  # Obtém o grupo "Cliente"
            user.groups.add(group)  # Adiciona o usuário ao grupo "Cliente"
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# def register(request):
#     form = CustomUserCreationForm()
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#
#             usuario = form.cleaned_data['usuario']
#             senha = form.cleaned_data['senha']
#             confirmar_senha = form.cleaned_data['confirmar_senha']
#             nome = form.cleaned_data['nome']
#             cpf = form.cleaned_data['cpf']
#             endereco = form.cleaned_data['endereco']
#             telefone = form.cleaned_data['telefone']
#             email = form.cleaned_data['email']
#
#             if senha == confirmar_senha:
#                 user = User(
#                     usuario=usuario,
#                     nome=nome,
#                     cpf=cpf,
#                     endereco=endereco,
#                     telefone=telefone,
#                     email=email,
#                 )
#                 user.groups.add(Group.objects.get(name="cliente"))
#                 user.set_password(senha)
#                 user.save()
#
#                 if usuario:
#                     return redirect('logi')
#
#                 else:
#                     print('invalid registration details')
#             else:
#                 messages.error(request, 'Senhas não batem')
#
#     else:
#         form = CustomUserCreationForm()
#
#     return render(request, "registration/register.html", {"form": form})


# def login_user(request):
#     if request.method == "POST":
#         form = CustomLoginForm(data=request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data['username']
#             senha = form.cleaned_data['password']
#             backend1 = CustomBackend()
#             user = backend1.authenticate_user(request, username=usuario, password=senha)
#             print(user)
#             if user:
#                 login(request, user, backend='accounts.backend.CustomBackend')
#                 return redirect('home')
#             else:
#                 return HttpResponse('Usuário ou senha inválidos')
#     else:
#         form = CustomLoginForm()
#
#     return render(request, 'registration/login.html', {'form': form})



