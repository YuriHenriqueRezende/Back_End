# Generated by Django 4.2.4 on 2023-08-29 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meuApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='residents',
        ),
        migrations.AddField(
            model_name='character',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='meuApp.location'),
        ),
        migrations.AddField(
            model_name='episode',
            name='character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Character', to='meuApp.character'),
        ),
    ]