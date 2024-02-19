from django.db import models
from django.utils import timezone

# se declara un modelo por tabla
# se declara una clase por tabla

class Sesion(models.Model):
    dni = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.dni

    class Meta:
        db_table = 'sesion'


class Persona(models.Model):
    dni = models.IntegerField(primary_key=True)
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dni}'

    class Meta:
        db_table = 'clientes'


class Raza(models.Model):
    idraza = models.IntegerField(primary_key=True)
    # You need to specify the max_length for this field.
    raza = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'{self.idraza}'

    class Meta:
        db_table = 'razas'


class Especie(models.Model):
    idespecie = models.IntegerField(primary_key=True)
    especie = models.CharField(max_length=20, default='')
    # Assuming idespecie is a foreign key to Especie.
    idraza = models.ForeignKey(
        Raza, db_column='idraza', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.idespecie}'

    class Meta:
        db_table = 'especies'


# OneToOneField representar la relacion entre Paciente y Persona
# on_delete=models.CASCADEdice a Django que active en cascada el efecto de eliminación, es decir,
# continúe eliminando también los modelos dependientes.
class Paciente(models.Model):
    idpaciente = models.AutoField(primary_key=True)
    dni = models.ForeignKey(
        Persona, db_column='dni', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    idraza = models.ForeignKey(
        Raza, on_delete=models.CASCADE, db_column='idraza')
    idespecie = models.ForeignKey(
        Especie, on_delete=models.CASCADE, db_column='idespecie')
    sexo = models.CharField(max_length=10)
    seniaspart = models.CharField(max_length=50)
    chip = models.CharField(max_length=20, blank=True, null=True)
  # Allow null values
    fechana = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.idpaciente}'

    class Meta:
        db_table = 'pacientes'



class Event(models.Model):
    idturno = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, blank=True)

    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=255)
  
    def __str__(self):
        return f'{self.dni} - {self.fecha} - {self.hora}'

    class Meta:
        db_table = 'turnos'


class Peso(models.Model):
    idpeso = models.AutoField(primary_key=True)
    peso = models.CharField(max_length=20)
    # Assuming idespecie is a foreign key to Especie.
  
    def __str__(self):
        return f'{self.idpeso}'  # Corrige aquí para que coincida con el nombre del campo

    class Meta:
        db_table = 'peso'


class Vacunas(models.Model):
    idvacuna = models.IntegerField(primary_key=True)
    vacuna = models.CharField(max_length=100)
    # Assuming idespecie is a foreign key to Especie.
    laboratorio = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.vacuna}'

    def __str__(self):
        return f'{self.idvacuna}'

    class Meta:
        db_table = 'vacunas'




class ExamenCli(models.Model):
    idexamenc = models.AutoField(primary_key=True)
    ganglios = models.CharField(max_length=20)
    mucosas = models.CharField(max_length=20)
    temperatura = models.CharField(max_length=20)
    cardiaca = models.CharField(max_length=20)
    pulso = models.CharField(max_length=20)
    respiratoria = models.CharField(max_length=20)
    # Assuming idespecie is a foreign key to Especie.
   

    def __str__(self):
        return f'{self.idexamenc}'

    class Meta:
        db_table = 'examenclinico'



class Historial(models.Model):
    idhistorial = models.IntegerField(primary_key=True)
    idpaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    fecha = models.DateField()
    fechadesp = models.DateField()
    productodesp = models.CharField(max_length=100)
    idvacuna = models.ForeignKey(Vacunas, on_delete=models.CASCADE, db_column='idvacuna')
    lotev = models.CharField(max_length=100)
    fechacelo = models.DateField()
    fechapart = models.DateField()
    estirilizado = models.CharField(max_length=10)
    consulta = models.TextField()
    hallazgo = models.TextField()
    idexamenc = models.ForeignKey(ExamenCli, on_delete=models.CASCADE, db_column='idexamenc')
    idpeso = models.ForeignKey(Peso, on_delete=models.CASCADE, db_column='idpeso')

    def __str__(self):
        return f'{self.idhistorial} ({self.idpaciente})'

    class Meta:
        db_table = 'historial'