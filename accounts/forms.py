from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


# class CustomUserCreationForm(forms.Form):
#     usuario = forms.CharField(label='Usuário', max_length=100)
#     nome = forms.CharField(max_length=100, label="Nome Completo")
#     cpf = forms.CharField(max_length=30)
#     endereco = forms.CharField(max_length=50)
#     telefone = forms.CharField(max_length=20)
#     email = forms.EmailField(max_length=100)
#     senha = forms.CharField(label='Senha', widget=forms.PasswordInput())
#     confirmar_senha = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#
#
# class CustomLoginForm(forms.Form):
#     username = forms.CharField(label='Usuário', max_length=100)
#     password = forms.CharField(label='Senha', widget=forms.PasswordInput())







