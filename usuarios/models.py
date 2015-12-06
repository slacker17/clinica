from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    curp = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=True,null=True)
    fecha_ingreso = models.DateField(blank=True,null=True)
    edad = models.IntegerField(blank=True,null=True)
    sexo = models.CharField(max_length=10)
    direccion = models.CharField(max_length=40)
    peso = models.FloatField(blank=True,null=True)
    estatura = models.FloatField(blank=True,null=True)
    diagnostico = models.CharField(max_length=100)
    mejorias = models.CharField(max_length=100,default="")
    enfermedad = models.CharField(max_length=30,default="")
    tratamiento = models.CharField(max_length=30,default="")
    
    class Meta:
        ordering=["nombre"]
        
    def __str__(self):
        return self.nombre
    
    
