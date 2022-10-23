# Generated by Django 4.0.5 on 2022-10-22 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fractionsstats',
            options={'ordering': ['-rating', '-games'], 'verbose_name': 'винрейт фракции', 'verbose_name_plural': 'винрейт фракций'},
        ),
        migrations.RemoveField(
            model_name='fractionsstats',
            name='description',
        ),
        migrations.RemoveField(
            model_name='playersstats',
            name='description',
        ),
        migrations.CreateModel(
            name='PlayersDescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='История оказалась пуста ¯\\_(ツ)_/¯', verbose_name='Описание')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stats.playersstats', verbose_name='Игрок')),
            ],
            options={
                'verbose_name': 'описание игры',
                'verbose_name_plural': 'описание игр игроков',
                'ordering': ['player'],
            },
        ),
        migrations.CreateModel(
            name='FractionsDescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='История оказалась пуста ¯\\_(ツ)_/¯', verbose_name='Описание')),
                ('fraction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stats.fractionsstats', verbose_name='Фракция')),
            ],
            options={
                'verbose_name': 'описание игры',
                'verbose_name_plural': 'описание игр фракций',
                'ordering': ['fraction'],
            },
        ),
    ]