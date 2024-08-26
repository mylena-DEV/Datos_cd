from django.db import models

    
GENERO = [
    ('M','M'),
    ('F','F'),
]
    
    
ESTADO_CIVIL = [
    ('Casado','Casado'),
    ('Soltero','Soltero'),
]    

        
class Ciudad (models.Model):
    Ciudad_Actual = models.CharField(max_length=50,null=False)
    class Meta: 
        verbose_name = 'Ciudad Actual'
        verbose_name_plural = 'Ciudad Actual'
    def __str__(self):
        return self.Ciudad_Actual
    
class Lugar_Nacimiento (models.Model):
    Ciudad_de_nacimiento = models.CharField(max_length=50,null=False)
    class Meta: 
        verbose_name = 'Nombre de la Ciudad'
        verbose_name_plural = 'Nombre de la Ciudad'
    def __str__(self):
        return self.Ciudad_de_nacimiento

class Datos (models.Model):
    class Meta: 
        verbose_name = 'Datos Generales'
        verbose_name_plural = 'Datos Generales'
    nombres = models.CharField(max_length=50,null=False)
    apellidos = models.CharField(max_length=50,null=False)
    direccion = models.CharField(max_length=50,null=False)
    telefono = models.CharField(max_length=50,null=False)
    provincia = models.CharField(max_length=50,null=False)
    correo = models.CharField(max_length=50,null=False)
    fecha_nacimiento = models.CharField(max_length=50,null=False)
    Sexo = models.CharField(max_length=50,choices=GENERO,verbose_name='Genero')
    EstadoCivil = models.CharField(max_length=50,choices=ESTADO_CIVIL,verbose_name='Estado civil')
    Ciudad_Actual = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    Nombre_Lugar = models.ForeignKey(Lugar_Nacimiento,on_delete=models.CASCADE)
# Create your models here.
