# Generated by Django 4.2.3 on 2023-07-22 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locacao', '0002_locacao_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='locacao',
            name='hora_devolucao',
            field=models.TimeField(default=datetime.datetime(2023, 7, 22, 15, 14, 14, 498963, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='locacao',
            name='hora_locacao',
            field=models.TimeField(default=datetime.datetime(2023, 7, 22, 15, 14, 14, 497974, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='locacao',
            name='data_devolucao',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Data de Devolução'),
        ),
        migrations.AlterField(
            model_name='locacao',
            name='data_locacao',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Data de Locação'),
        ),
    ]
