from django.db import models

class Formulario(models.Model):
    Tipo_Vinculacion = models.CharField(max_length=100)
    Proceso = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)
    Licencia_infobip = models.CharField(max_length=50, blank=True, null=True)
    Estado = models.CharField(max_length=50)
    Telefono_corporativo =models.CharField(max_length=20, blank=True, null=True)
    Telefono_personal = models.CharField(max_length=20)
    CC = models.CharField(max_length=20, unique=True)
    Nombre = models.CharField(max_length=150)
    Usuario_red = models.CharField(max_length=50, unique=True)
    Login = models.CharField(max_length=50)
    ID_unidad = models.CharField(max_length=50)
    GID = models.CharField(max_length=50)
    Fecha_ingreso = models.DateField()
    Correo = models.EmailField(unique=True)
    Fecha_cumpleaños = models.DateField()
    Antiguedad = models.CharField(max_length=50, blank=True, null=True)
    Horario = models.CharField(max_length=100)
    Usuario_recaudo_masivo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    
