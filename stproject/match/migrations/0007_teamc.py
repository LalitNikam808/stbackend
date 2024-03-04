# Generated by Django 5.0.2 on 2024-03-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0006_teamb'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamC',
            fields=[
                ('match_time', models.BigIntegerField(primary_key=True, serialize=False)),
                ('game_time', models.TimeField(unique=True)),
                ('start_game', models.CharField(blank=True, max_length=50, null=True)),
                ('end_game', models.CharField(blank=True, max_length=50, null=True)),
                ('quater', models.CharField(blank=True, max_length=50, null=True)),
                ('tag', models.CharField(blank=True, max_length=50, null=True)),
                ('shot_type', models.CharField(blank=True, max_length=50, null=True)),
                ('made_sjn', models.CharField(blank=True, max_length=50, null=True)),
                ('made_sloc', models.JSONField(blank=True, null=True)),
                ('made_ajn', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_type', models.CharField(blank=True, max_length=50, null=True)),
                ('reb_type', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_off_jn', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_off_loc', models.JSONField(blank=True, null=True)),
                ('miss_def_jn', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_def_loc', models.JSONField(blank=True, null=True)),
                ('foul_type', models.CharField(blank=True, max_length=50, null=True)),
                ('shot_foul', models.CharField(blank=True, max_length=50, null=True)),
                ('made_wf_sjn', models.CharField(blank=True, max_length=50, null=True)),
                ('made_wf_sloc', models.JSONField(blank=True, null=True)),
                ('made_wf_ajn', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_wf_sjn', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_wf_sloc', models.JSONField(blank=True, null=True)),
                ('miss_wf_djn', models.CharField(blank=True, max_length=50, null=True)),
                ('miss_wf_dloc', models.JSONField(blank=True, null=True)),
                ('player_in_jn', models.CharField(blank=True, max_length=50, null=True)),
                ('player_out_jn', models.CharField(blank=True, max_length=50, null=True)),
                ('turnover_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
