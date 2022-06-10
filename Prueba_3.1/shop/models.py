from django.db import models

# Create your models here.
class Contacto(models.Model):
    nomContacto = models.CharField(max_length=200,verbose_name='Nombre')
    apeContacto = models.CharField(max_length=200,verbose_name='Apellido')
    rutContacto = models.CharField(primary_key=True, max_length=9,verbose_name='Rut')
    telContacto = models.IntegerField(verbose_name='Teléfono')
    CorreoContacto = models.CharField(max_length=200,verbose_name='Correo')
    ComenContacto = models.CharField(max_length=255,verbose_name='Comentario')


    def __str__(self):
        return self.nomContacto
    def __str__(self):
        return self.apeContacto
    def __str__(self):
        return self.rutContacto
    def __str__(self):
        return self.telContacto
    def __str__(self):
        return self.CorreoContacto
    def __str__(self):
        return self.ComenContacto