# Generated by Django 4.2.3 on 2024-01-04 02:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_historial_peso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historial',
            old_name='cons',
            new_name='estirilizado',
        ),
        migrations.RenameField(
            model_name='historial',
            old_name='est',
            new_name='hallazgo',
        ),
        migrations.RenameField(
            model_name='peso',
            old_name='peso',
            new_name='pesoT',
        ),
        migrations.RemoveField(
            model_name='historial',
            name='hall',
        ),
        migrations.RemoveField(
            model_name='historial',
            name='proddesp',
        ),
        migrations.AddField(
            model_name='historial',
            name='consulta',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='historial',
            name='productodesp',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='examencli',
            name='idexamenc',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='historial',
            name='fechacelo',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='historial',
            name='fechadesp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='historial',
            name='fechapart',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='contrasena',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='examencli',
            table='examenclinico',
        ),
        migrations.AlterModelTable(
            name='historial',
            table='historial',
        ),
        migrations.AlterModelTable(
            name='vacunas',
            table='vacunas',
        ),
    ]
