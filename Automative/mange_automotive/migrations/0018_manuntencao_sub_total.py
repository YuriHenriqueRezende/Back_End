# Generated by Django 4.2.3 on 2023-10-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mange_automotive', '0017_remove_manuntencao_logistica_fk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuntencao',
            name='sub_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]