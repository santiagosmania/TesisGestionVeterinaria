# Generated by Django 4.2.3 on 2024-01-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_event_idturno_alter_event_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='idturno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='event',
            table='turnos',
        ),
    ]