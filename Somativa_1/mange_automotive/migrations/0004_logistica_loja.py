# Generated by Django 4.2.3 on 2023-10-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mange_automotive', '0003_categoria_servico'),
    ]

    operations = [
        migrations.CreateModel(
            name='logistica_loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('patrimonio', models.DecimalField(decimal_places=2, max_digits=120)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
