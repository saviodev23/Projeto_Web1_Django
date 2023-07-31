from .models import User
from django import forms


class CustomUserCreationForm(forms.Form):
    usuario = forms.CharField(label='Usuário', max_length=100)
    nome = forms.CharField(max_length=100, label="Nome Completo")
    cpf = forms.CharField(max_length=30)
    endereco = forms.CharField(max_length=50)
    telefone = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput())
    confirmar_senha = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput())

    class Meta:
        model = User


class CustomLoginForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())




