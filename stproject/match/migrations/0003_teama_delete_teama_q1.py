# Generated by Django 5.0.2 on 2024-02-27 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_remove_teama_q1_id_alter_teama_q1_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamA',
            fields=[
                ('time', models.BigIntegerField(primary_key=True, serialize=False)),
                ('shot', models.CharField(max_length=50)),
                ('made', models.CharField(blank=True, max_length=50, null=True)),
                ('made_SJN', models.CharField(blank=True, max_length=50, null=True)),
                ('made_locx', models.FloatField(blank=True, null=True)),
                ('made_locy', models.FloatField(blank=True, null=True)),
                ('made_assist', models.CharField(blank=True, max_length=50, null=True)),
                ('made_shottype', models.CharField(blank=True, max_length=50, null=True)),
                ('miss', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_outb', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_reb', models.CharField(blank=True, max_length=50, null=True)),
                ('o_reb_SJN', models.CharField(blank=True, max_length=50, null=True)),
                ('d_reb_DJN', models.CharField(blank=True, max_length=50, null=True)),
                ('quater', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TeamA_Q1',
        ),
    ]
