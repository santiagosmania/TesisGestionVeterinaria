# Generated by Django 4.2.3 on 2024-01-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_historial_fecha_alter_historial_fechacelo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateField(),
        ),
    ]