# Generated by Django 4.0.4 on 2022-07-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_players_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winrateplayersstats',
            name='games',
            field=models.BigIntegerField(verbose_name='Финалок игрока'),
        ),
        migrations.AlterField(
            model_name='winrateplayersstats',
            name='winrate',
            field=models.BigIntegerField(verbose_name='Винрейт игрока'),
        ),
        migrations.DeleteModel(
            name='Players',
        ),
    ]
