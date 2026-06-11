from datetime import datetime
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()
  
    

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Cedula: {self.obtener_provincia()} - Edad: {self.edad} - Año de Nacimiento: {self.obtener_anio()}"

    def obtener_anio(self):
        anio_actual = datetime.now().year
        valor = anio_actual - self.edad
        return valor
    
# saber la provincia por num cedula, si empieza en 11 es de loja sino es de otra ciudad
    def obtener_provincia(self):
        if self.cedula.startswith('11'):
            return "Loja"
        return "Otra ciudad"
    


