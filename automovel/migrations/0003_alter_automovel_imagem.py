# Generated by Django 4.2.3 on 2023-07-20 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automovel', '0002_automovel_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovel',
            name='imagem',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
    ]
