# Generated by Django 2.2.6 on 2019-10-21 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compagnie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='statut',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='titre',
            name='statut',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ville',
            name='statut',
            field=models.BooleanField(default=True),
        ),
    ]
