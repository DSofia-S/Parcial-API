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

# EDITORIAL
class Editorial(models.Model):
    Id_Editorial = models.AutoField(primary_key=True, editable=False, db_column='T002IdEditorial')
    Nombre = models.CharField(max_length=100, db_column='T002Nombre')
    Direccion = models.CharField(max_length=200, db_column='T002Direccion')
    Telefono = models.CharField(max_length=15, db_column='T002Telefono')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table='T002Editorial'
        verbose_name='Editorial'
        verbose_name_plural='Editoriales'
        
# LIBRO
class Libro(models.Model):
    Id_Libro = models.AutoField(primary_key=True, editable=False, db_column='T003IdLibro')
    Titulo = models.CharField(max_length=100, db_column='T003Titulo')
    Resumen = models.CharField(max_length=500, db_column='T003Resumen')
    ISBN = models.CharField(max_length=13, unique=True, db_column='T003ISBN')
    Año_Pub = models.DateField(db_column='T003Año')
    Id_Autor = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='T003IdAutor')
    Id_Editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, db_column='T003IdEditorial')

    def __str__(self):
        return f"{self.Titulo}"

    class Meta:
        db_table='T003Titulo'
        verbose_name='Titulo'
        verbose_name_plural='Titulos'

# MIEMBRO
class Miembro(models.Model):
    Id_Miembro = models.AutoField(primary_key=True, editable=False, db_column='T004IdMiembro')
    Nombre = models.CharField(max_length=100, db_column='T004Nombre')
    Apellido = models.CharField(max_length=100, db_column='T004Apellido')
    Email = models.CharField(max_length=10, db_column='T004Email')
    Fecha_Mem = models.DateField(db_column='T004Fecha')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table='T004Miembro'
        verbose_name='Miembro'
        verbose_name_plural='Miembros'
