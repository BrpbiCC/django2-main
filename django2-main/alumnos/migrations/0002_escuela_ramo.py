# Generated by Django 5.0.6 on 2024-06-01 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id_escuela', models.IntegerField(db_column='idEscuela ', primary_key=True, serialize=False)),
                ('escuela', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id_ramo', models.AutoField(db_column='idRamo', primary_key=True, serialize=False)),
                ('ramo', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
                ('id_escuela', models.ForeignKey(db_column='idEscuela', on_delete=django.db.models.deletion.CASCADE, to='alumnos.escuela')),
            ],
        ),
    ]
