# Generated by Django 4.2.3 on 2023-07-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_email_alter_user_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usuario',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
