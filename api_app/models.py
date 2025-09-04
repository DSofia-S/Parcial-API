from django.db import models

# Create your models here.
# AUTOR
class Autor(models.Model):
    Id_Autor = models.AutoField(primary_key=True, editable=False, db_column='T001IdAutor')
    Nombre = models.CharField(max_length=100, db_column='T001Nombre')
    Apellido = models.CharField(max_length=100, db_column='T001Apellido')
    Biografia = models.CharField(max_length=500, db_column='T001Biografia')

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"

    class Meta:
        db_table='T001Autor'
        verbose_name='Autor'
        verbose_name_plural='Autores'
