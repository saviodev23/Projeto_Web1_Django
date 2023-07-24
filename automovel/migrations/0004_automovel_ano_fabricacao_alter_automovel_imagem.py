# Generated by Django 4.2.3 on 2023-07-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automovel', '0003_alter_automovel_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='automovel',
            name='ano_fabricacao',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='automovel',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
