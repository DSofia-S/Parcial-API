from django.urls import path
from .views import AutorList, CrearAutor, ActualizarAutor, EliminarAutor, CrearEditorial, EditorialList, ActualizarEditorial, EliminarEditorial, CrearLibro, LibroList, ActualizarLibro, EliminarLibro, CrearMiembro, MiembrosList, ActualizarMiembro, EliminarMiembro,Prestamo, CrearPrestamo, PrestamosList, ActualizarPrestamos, EliminarPrestamo, LibroByAutor, librobyeditorial,pertamobyfecha


urlpatterns = [
    path('autores/', AutorList.as_view(), name='persona-list'),
    path('autores/crear/', CrearAutor.as_view(), name='crear-autor'),
    path('autores/actualizar/<int:pk>/', ActualizarAutor.as_view(), name='actualizar-autor'),
    path('autores/eliminar/<int:pk>/', EliminarAutor.as_view(), name='eliminar-autor'),
    path('editoriales/', EditorialList.as_view(), name='editorial-list'),
    path('editoriales/crear/', CrearEditorial.as_view(), name='crear-editorial'),
    path('editoriales/actualizar/<int:pk>/', ActualizarEditorial.as_view(), name='actualizar-editorial'),
    path('editoriales/eliminar/<int:pk>/', EliminarEditorial.as_view(), name='eliminar-editorial'),
    path('libros/', LibroList.as_view(), name='libro-list'),
    path('libros/crear/', CrearLibro.as_view(), name='crear-libro'),
    path('libros/actualizar/<int:pk>/', ActualizarLibro.as_view(), name='actualizar-libro'),
    path('libros/eliminar/<int:pk>/', EliminarLibro.as_view(), name='eliminar-libro'),
    path('miembros/', MiembrosList.as_view(), name='miembro-list'),
    path('miembros/crear/', CrearMiembro.as_view(), name='crear-miembro'),
    path('miembros/actualizar/<int:pk>/', ActualizarMiembro.as_view(), name='actualizar-miembro'),
    path('miembros/eliminar/<int:pk>/', EliminarMiembro.as_view(), name='eliminar-miembro'),
    path('prestamos/', PrestamosList.as_view(), name='prestamo-list'),
    path('prestamos/crear/', CrearPrestamo.as_view(), name='crear-prestamo'),
    path('prestamos/actualizar/<int:pk>/', ActualizarPrestamos.as_view(), name='actualizar-prestamo'),
    path('prestamos/eliminar/<int:pk>/', EliminarPrestamo.as_view(), name='eliminar-prestamo'),
    path('libros/autor/<str:Nombre>/', LibroByAutor.as_view(), name='libro-by-autor'),
    path('libros/editorial/<str:Nombre>/', librobyeditorial.as_view(), name='libro-by-editorial'),
]