# Generated by Django 2.2.2 on 2019-10-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='adresse',
            field=models.CharField(default='rue de la lib', max_length=100),
        ),
    ]
