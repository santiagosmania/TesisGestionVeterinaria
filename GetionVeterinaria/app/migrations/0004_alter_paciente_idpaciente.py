# Generated by Django 4.2.3 on 2023-10-25 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_sesion_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='idpaciente',
            field=models.IntegerField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
