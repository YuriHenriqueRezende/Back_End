# Generated by Django 4.2.3 on 2023-10-14 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mange_automotive', '0031_remove_reserva_nome_fk_reserva_manuntencao_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
