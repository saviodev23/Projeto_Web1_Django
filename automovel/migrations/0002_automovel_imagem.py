# Generated by Django 4.2.3 on 2023-07-20 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automovel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automovel',
            name='imagem',
            field=models.ImageField(default='', upload_to='images/%Y/%m/%d/'),
        ),
    ]
