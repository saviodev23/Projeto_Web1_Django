import datetime
import time
from django.db import models
from django.contrib.auth.models import User
from automovel.models import Automovel

class Locacao(models.Model):
    STATUS_LOCACAO = (
        ('Pendente', 'Pendente'),
        ('Retirado', 'Retirado'),
        ('Cancelado', 'Cancelado'),
        ('Devolvido','Devolvido'),
    )

    data_locacao = models.DateField(verbose_name='Data de Locação', default=datetime.date)
    data_devolucao = models.DateField(verbose_name='Data de Devolução', default=datetime.date)
    hora_locacao = models.TimeField(verbose_name='Hora de Locação', default=time.time())
    hora_devolucao = models.TimeField(verbose_name='Hora de Devolução', default=time.time())
    quilometragem = models.IntegerField(default=0)
    valor_locacao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Preço de Locação')
    devolvido = models.BooleanField(blank=True, null=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    limite_km_dia = models.IntegerField(default=100)
    status = models.CharField(max_length=12, choices=STATUS_LOCACAO, default='Pendente')
    automovel = models.ForeignKey(Automovel, on_delete=models.CASCADE)
