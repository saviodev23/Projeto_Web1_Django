from django.forms import ModelForm
from automovel.models import Automovel, Modelo,Marca
from django import forms

class FormAddAutomovel(ModelForm):
    widgets = {
        'imagem': forms.FileInput(attrs={'id': 'upload', 'accept': "image/*", 'required': True})
    }
    class Meta:
        model = Automovel
        fields = "__all__"

class FormAddMarca(ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"

class FormAddModelo(ModelForm):
    class Meta:
        model = Modelo
        fields = "__all__"