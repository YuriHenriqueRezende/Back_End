# Generated by Django 4.2.3 on 2023-10-14 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mange_automotive', '0030_categoria_automovel_dono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='nome_fk',
        ),
        migrations.AddField(
            model_name='reserva',
            name='manuntencao_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manu', to='mange_automotive.manuntencao'),
        ),
    ]
