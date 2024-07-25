# Generated by Django 5.0.6 on 2024-05-19 01:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_final', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='pecas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('imagem', models.CharField(max_length=200)),
                ('medida', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=200)),
                ('parcelamento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('imagem', models.CharField(max_length=200)),
                ('peso', models.IntegerField()),
                ('medida', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=200)),
                ('score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('parcelamento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frete', models.IntegerField()),
                ('forma_pagamento', models.CharField(choices=[('P', 'PIX'), ('D', 'DEBITO'), ('C', 'CREDITO'), ('B', 'BOLETO'), ('V', 'VALE PRESENTE')], max_length=100)),
                ('cupom', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('P', 'Pendente'), ('C', 'Cancelado(a)'), ('A', 'Aprovado(a)')], default='P', max_length=100)),
                ('valor_carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinhoFKFK', to='app.carrinho')),
            ],
        ),
        migrations.CreateModel(
            name='pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentoFKFK', to='app.pagamento')),
            ],
        ),
        migrations.CreateModel(
            name='imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=200)),
                ('produtoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagemFKFK', to='app.produto')),
            ],
        ),
        migrations.AddField(
            model_name='carrinho',
            name='produtoFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtoFKFK', to='app.produto'),
        ),
        migrations.CreateModel(
            name='sub_produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pecasFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pecasFKFK', to='app.pecas')),
            ],
        ),
    ]