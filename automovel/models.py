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
    COR_CHOICES = (
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
        ('Prata', 'Prata'),
        ('Vermelho', 'Vermelho'),
        ('Azul', 'Azul'),
        ('Verde', 'Verde'),
        ('Amarelo', 'Amarelo'),
        ('Laranja', 'Laranja'),
        ('Rosa', 'Rosa'),
        ('Roxo', 'Roxo'),
    )
    TIPO_COMBUSTIVEL_CHOICES = (
        ('Gasolina', 'Gasolina'),
        ('Etanol', 'Etanol'),
        ('Diesel', 'Diesel'),
        ('Flex', 'Flex'),
        ('Eletrico', 'Elétrico'),
    )

    placa = models.CharField(max_length=10)
    cor = models.CharField(max_length=20, choices=COR_CHOICES, default='Branco')
    nr_portas = models.IntegerField(verbose_name='Número de portas', default=4)
    tipo_combustivel = models.CharField(max_length=10, choices=TIPO_COMBUSTIVEL_CHOICES, default='Flex')
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





