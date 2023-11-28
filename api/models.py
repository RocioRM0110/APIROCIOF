from django.db import models


# Create your models here.
<<<<<<< HEAD
=======
# class Registro(models.Model):
#     idRegistro = models.IntegerField(primary_key=True, db_column='idRegistro')
#     usuario = models.CharField(max_length=100, db_column='usuario')
#     correo = models.EmailField(db_column='correo')
#     password = models.CharField(max_length=100, db_column='password')
#     class Meta:
#         db_table='Usuarios'

# models.py



>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b
class Registro(models.Model):
    idRegistro = models.IntegerField(primary_key=True, db_column='idRegistro')
    usuario = models.CharField(max_length=100, db_column='usuario')
    correo = models.EmailField(db_column='correo')
    password = models.CharField(max_length=100, db_column='password')
<<<<<<< HEAD
    class Meta:
        db_table='Usuarios'

=======

    class Meta:
        db_table = 'Usuarios'

    def __str__(self):
        return f'{self.usuario} ({self.correo})'

# class Preguntas(models.Model):
#     id_respuesta = models.AutoField(primary_key=True, db_column='id_respuesta')
#     descripcion = models.CharField(max_length=255, db_column='P1')
#     descripcion1 = models.CharField(max_length=255, db_column='P2')
#     descripcion2 = models.CharField(max_length=255, db_column='P3')
#     descripcion3 = models.CharField(max_length=255, db_column='P4')
#     descripcion4 = models.CharField(max_length=255, db_column='P5')
#     descripcion5 = models.CharField(max_length=255, db_column='P6')
#     descripcion6 = models.CharField(max_length=255, db_column='P7')
#     descripcion7 = models.CharField(max_length=255, db_column='P8')
#     descripcion8 = models.CharField(max_length=255, db_column='P9')
#     descripcion9 = models.CharField(max_length=255, db_column='P10')
#     descripcion10 = models.CharField(max_length=255, db_column='P11')
    
#     class Meta:
#         db_table='Services'
>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b
class Preguntas(models.Model):
    id_respuesta = models.AutoField(primary_key=True, db_column='id_respuesta')
    descripcion = models.CharField(max_length=255, db_column='P1')
    descripcion1 = models.CharField(max_length=255, db_column='P2')
    descripcion2 = models.CharField(max_length=255, db_column='P3')
    descripcion3 = models.CharField(max_length=255, db_column='P4')
    descripcion4 = models.CharField(max_length=255, db_column='P5')
    descripcion5 = models.CharField(max_length=255, db_column='P6')
    descripcion6 = models.CharField(max_length=255, db_column='P7')
    descripcion7 = models.CharField(max_length=255, db_column='P8')
    descripcion8 = models.CharField(max_length=255, db_column='P9')
    descripcion9 = models.CharField(max_length=255, db_column='P10')
    descripcion10 = models.CharField(max_length=255, db_column='P11')
    
    class Meta:
<<<<<<< HEAD
        db_table='Services'
=======
        db_table = 'Services'

    def __str__(self):
        return self.descripcion

>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b
