# Generated by Django 4.2.3 on 2023-10-07 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mange_automotive', '0018_manuntencao_sub_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manuntencao',
            name='mao_obra',
        ),
    ]