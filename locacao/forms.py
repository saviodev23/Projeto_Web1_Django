from django import forms
from django.contrib.auth.models import User

from locacao.models import Locacao


class FormAddLocacao(forms.Form):
    data_locacao = forms.DateField(label='Data de Locação')
    data_devolucao = forms.DateField(label='Data de Devolução')
    hora_locacao = forms.TimeField(label='Hora de Locação')
    hora_devolucao = forms.TimeField(label='Hora de Devolução')



class FormEditLocacao(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['status', 'data_locacao', 'hora_locacao', 'data_devolucao', 'hora_devolucao', 'automovel', 'valor_locacao', 'quilometragem']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'data_locacao': forms.DateInput(attrs={'class': 'form-control'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control'}),
            'hora_locacao': forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_devolucao': forms.TimeInput(attrs={'class': 'form-control'}),
            'automovel': forms.Select(attrs={'class': 'form-control'}),
            'valor_locacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'quilometragem': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FormAdminLocacao(forms.ModelForm):
    STATUS_LOCACAO = (
        ('Pendente', 'Pendente'),
        ('Retirado', 'Retirado'),
        ('Cancelado', 'Cancelado'),
        ('Devolvido','Devolvido'),
    )
    data_locacao = forms.DateField()
    hora_locacao = forms.TimeField()
    data_devolucao = forms.DateField()
    hora_devolucao = forms.TimeField()
    status = forms.ChoiceField(choices=STATUS_LOCACAO)

    class Meta:
        model = Locacao
        fields = ['data_locacao', 'hora_locacao', 'data_devolucao', 'hora_devolucao', 'cliente', 'status']
