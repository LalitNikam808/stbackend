# Generated by Django 5.0.2 on 2024-03-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0012_rename_quater_teamb_quarter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teama',
            name='game_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='teamb',
            name='game_time',
            field=models.TimeField(),
        ),
    ]
