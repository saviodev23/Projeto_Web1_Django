from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=30, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='usuarios'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios'
    )
    USERNAME_FIELD = 'usuario'

    def __str__(self) -> str:
        return self.username