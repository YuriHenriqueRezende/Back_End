# Generated by Django 4.2.3 on 2023-09-21 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0003_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='CPF',
            field=models.IntegerField(),
        ),
    ]