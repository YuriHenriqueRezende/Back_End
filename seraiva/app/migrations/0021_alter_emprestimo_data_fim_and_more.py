# Generated by Django 5.0.6 on 2024-05-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_emprestimo_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]