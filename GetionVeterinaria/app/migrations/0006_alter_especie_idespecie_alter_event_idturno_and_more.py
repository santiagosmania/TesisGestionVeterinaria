# Generated by Django 4.2.3 on 2023-10-25 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_paciente_idpaciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='idespecie',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='idturno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='raza',
            name='idraza',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]