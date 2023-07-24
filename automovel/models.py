from django.db import models
class Marca(models.Model):
    descricao = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.descricao
class Modelo(models.Model):
    descricao = models.CharField(max_length=20, blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Automovel(models.Model):
    TIPO_COMBUSTIVEL_CHOICES = (
        ('gasolina', 'Gasolina'),
        ('etanol', 'Etanol'),
        ('diesel', 'Diesel'),
        ('flex', 'Flex'),
        ('eletrico', 'Elétrico'),
    )

    placa = models.CharField(max_length=10, blank=True, null=True)
    cor = models.CharField(max_length=20, blank=True, null=True)
    nr_portas = models.IntegerField(verbose_name='Número de portas', blank=True, null=True)
    tipo_combustivel = models.CharField(max_length=10, choices=TIPO_COMBUSTIVEL_CHOICES, default='flex')
    quilometragem = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    renavam = models.IntegerField(blank=True, null=True)
    chassi = models.CharField(max_length=20, blank=True, null=True)
    ano_fabricacao = models.IntegerField(blank=False, null=False)
    descricao = models.TextField(max_length=300, default="")
    valor_locacao = models.DecimalField(blank=True, null=True, verbose_name='Preço de locação', max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    disponivel = models.BooleanField()

    def __str__(self):
        return self.modelo.marca.descricao





