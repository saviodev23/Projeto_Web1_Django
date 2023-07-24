from django.contrib.auth.backends import ModelBackend
from accounts.models import User
from django.contrib.auth.hashers import check_password


class CustomBackend(ModelBackend):
    def authenticate_user(self, request, username, password):
        try:
            # Obter todos os usuários com o username fornecido
            usuarios = User.objects.filter(username=username).first()
            print(usuarios)

            if check_password(password, usuarios.password):
                print('entrou')
                return usuarios

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None





# class CustomBackend(ModelBackend):
#     def authenticate_user(self, request, usuario, senha):
#         User = get_user_model()
#         try:
#             # Obter o usuário com o username fornecido
#             usuario_obj = User.objects.get(usuario=usuario)
#
#             if check_password(senha, usuario_obj.password):
#                 return usuario_obj
#
#         except User.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         User = get_user_model()
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None