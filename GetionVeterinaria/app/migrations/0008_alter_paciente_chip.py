# Generated by Django 4.2.3 on 2023-10-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_paciente_chip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='chip',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]