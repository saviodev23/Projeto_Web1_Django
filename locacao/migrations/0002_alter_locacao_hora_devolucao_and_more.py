# Generated by Django 4.2.3 on 2023-08-10 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locacao',
            name='hora_devolucao',
            field=models.TimeField(default=1691708891.7511842, verbose_name='Hora de Devolução'),
        ),
        migrations.AlterField(
            model_name='locacao',
            name='hora_locacao',
            field=models.TimeField(default=1691708891.7511842, verbose_name='Hora de Locação'),
        ),
    ]
