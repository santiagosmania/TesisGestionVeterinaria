# Generated by Django 4.2.3 on 2024-01-12 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_event_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='idpaciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paciente'),
        ),
    ]
