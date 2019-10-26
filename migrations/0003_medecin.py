# Generated by Django 2.2.2 on 2019-10-19 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_patient_adresse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('specialite', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('dateNaissance', models.DateTimeField()),
                ('adresse', models.CharField(default='rue de la lib', max_length=100)),
                ('tarif', models.PositiveSmallIntegerField()),
            ],
        ),
    ]