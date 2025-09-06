from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics , status
from rest_framework.exceptions import NotFound
from .serializers import AutorSerializer,EditorialSerializer,LibroSerializer,MiembroSerializer,PrestamoSerializer
from .models import Autor,Editorial,Libro,Miembro,Prestamo
from django.shortcuts import get_object_or_404

# Create your views here.

## CRUD AUTORES##
#Crear Autores
class CrearAutor(generics.CreateAPIView):
    queryset=Autor.objects.all()
    serializer_class=AutorSerializer

    def post(self, request):
        serializer=AutorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'seccess':True, 'detail':'Autor creado con éxito', 'data':serializer.data}, status=status.HTTP_201_CREATED)

# Lista Autor
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get(self, request):
        Autores=Autor.objects.all()
        serializer=AutorSerializer(Autores, many=True)
        if not Autores:
            raise NotFound("No se encontraron Autores")
        return Response ({'success': True, 'detail': 'Listado de autores', 'data': serializer.data}, status=status.HTTP_200_OK)
    
#Actualizar Autor
class ActualizarAutor(generics.UpdateAPIView):
    queryset=Autor.objects.all()
    serializer_class=AutorSerializer

    def put(self, request, pk):
        autor=get_object_or_404(Autor, pk=pk)
        serializer=AutorSerializer(autor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail':'Autor actualizado con éxito', 'data':serializer.data}, status=status.HTTP_200_OK)

#Eliminar Autor
class EliminarAutor(generics.DestroyAPIView):
    queryset=Autor.objects.all()
    serializer_class=AutorSerializer

    def delete(self, request, pk):
        autor=get_object_or_404(Autor, pk=pk)
        autor.delete()
        return Response({'success':True, 'detail':'Autor eliminado con éxito'}, status=status.HTTP_200_OK)

## CRUD EDITORIALES##
#Crear editoriales
class CrearEditorial(generics.CreateAPIView):
    queryset=Editorial.objects.all()
    serializer_class=EditorialSerializer

    def post(self, request):
        serializer=EditorialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'seccess':True, 'detail':'Editorial creada con éxito', 'data':serializer.data}, status=status.HTTP_201_CREATED)
    
#Lista de editoriales
class EditorialList(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def get(self, request):
        Editoriales=Editorial.objects.all()
        serializer=EditorialSerializer(Editoriales, many=True)
        if not Editoriales:
            raise NotFound("No se encontraron Editoriales")
        return Response ({'success': True, 'detail': 'Listado de editoriales', 'data': serializer.data}, status=status.HTTP_200_OK)
    
#Actualizar Editoriales
class ActualizarEditorial (generics.UpdateAPIView):
    queryset=Editorial.objects.all()
    serializer_class=EditorialSerializer

    def put(self, request, pk):
        editorial=get_object_or_404(Editorial, pk=pk)
        serializer=EditorialSerializer(editorial, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail':'Editorial actualizada con éxito', 'data':serializer.data}, status=status.HTTP_200_OK)
    
#Eliminar Editorial
class EliminarEditorial(generics.DestroyAPIView):
    queryset=Editorial.objects.all()
    serializer_class=EditorialSerializer

    def delete(self, request, pk):
        editorial=get_object_or_404(Editorial, pk=pk)
        editorial.delete()
        return Response({'success':True, 'detail':'Editorial eliminada con éxito'}, status=status.HTTP_200_OK)

## CRUD LIBROS##
#Crear Libros
class CrearLibro(generics.CreateAPIView):
    queryset=Libro.objects.all()
    serializer_class=LibroSerializer

    def post(self, request):
        serializer=LibroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'seccess':True, 'detail':'Libro creado con éxito', 'data':serializer.data}, status=status.HTTP_201_CREATED)
    
#Lista de libros
class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request):
        Libros=Libro.objects.all()
        serializer=LibroSerializer(Libros, many=True)
        if not Libros:
            raise NotFound("No se encontraron Libros")
        return Response ({'success': True, 'detail': 'Listado de libros', 'data': serializer.data}, status=status.HTTP_200_OK)
    
#Actualizar libros
class ActualizarLibro (generics.UpdateAPIView):
    queryset=Libro.objects.all()
    serializer_class=LibroSerializer

    def put(self, request, pk):
        libro=get_object_or_404(Libro, pk=pk)
        serializer=LibroSerializer(libro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail':'Libro actualizado con éxito', 'data':serializer.data}, status=status.HTTP_200_OK)
    
#Eliminar Libro
class EliminarLibro(generics.DestroyAPIView):
    queryset=Libro.objects.all()
    serializer_class=LibroSerializer

    def delete(self, request, pk):
        libro=get_object_or_404(Libro, pk=pk)
        libro.delete()
        return Response({'success':True, 'detail':'Libro eliminado con éxito'}, status=status.HTTP_200_OK)

## CRUD MIEMBROS##
#Crear Miembro
class CrearMiembro(generics.CreateAPIView):
    queryset=Miembro.objects.all()
    serializer_class=MiembroSerializer

    def post(self, request):
        serializer=MiembroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'seccess':True, 'detail':'Miembro creado con éxito', 'data':serializer.data}, status=status.HTTP_201_CREATED)
    
#Lista de miembros
class MiembrosList(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def get(self, request):
        Miembros=Miembro.objects.all()
        serializer=MiembroSerializer(Miembros, many=True)
        if not Miembros:
            raise NotFound("No se encontraron Miembros")
        return Response ({'success': True, 'detail': 'Listado de Miembros', 'data': serializer.data}, status=status.HTTP_200_OK)
    
#Actualizar Miembros
class ActualizarMiembro (generics.UpdateAPIView):
    queryset=Miembro.objects.all()
    serializer_class=MiembroSerializer

    def put(self, request, pk):
        miembro=get_object_or_404(Miembro, pk=pk)
        serializer=MiembroSerializer(miembro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail':'Miembro actualizado con éxito', 'data':serializer.data}, status=status.HTTP_200_OK)
    
#Eliminar Miembro
class EliminarMiembro(generics.DestroyAPIView):
    queryset=Miembro.objects.all()
    serializer_class=MiembroSerializer

    def delete(self, request, pk):
        miembro=get_object_or_404(Miembro, pk=pk)
        miembro.delete()
        return Response({'success':True, 'detail':'Miembro eliminado con éxito'}, status=status.HTTP_200_OK)


## CRUD PRESTAMO##
#Crear Prestamo
class CrearPrestamo(generics.CreateAPIView):
    queryset=Prestamo.objects.all()
    serializer_class=PrestamoSerializer

    def post(self, request):
        serializer=PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'seccess':True, 'detail':'Prestamo creado con éxito', 'data':serializer.data}, status=status.HTTP_201_CREATED)
    
#Lista de prestamos
class PrestamosList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get(self, request):
        Prestamos=Prestamo.objects.all()
        serializer=PrestamoSerializer(Prestamos, many=True)
        if not Prestamos:
            raise NotFound("No se encontraron Prestamos")
        return Response ({'success': True, 'detail': 'Listado de Prestamos', 'data': serializer.data}, status=status.HTTP_200_OK)
    
#Actualizar Prestamos
class ActualizarPrestamos (generics.UpdateAPIView):
    queryset=Prestamo.objects.all()
    serializer_class=PrestamoSerializer

    def put(self, request, pk):
        prestamo=get_object_or_404(Prestamo, pk=pk)
        serializer=PrestamoSerializer(prestamo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail':'Prestamo actualizado con éxito', 'data':serializer.data}, status=status.HTTP_200_OK)
    
#Eliminar Prestamo
class EliminarPrestamo(generics.DestroyAPIView):
    queryset=Prestamo.objects.all()
    serializer_class=PrestamoSerializer

    def delete(self, request, pk):
        prestamo=get_object_or_404(Prestamo, pk=pk)
        prestamo.delete()
        return Response({'success':True, 'detail':'Prestamo eliminado con éxito'}, status=status.HTTP_200_OK)

## FILTROS ##
# Buscar libros autor 
class LibroByAutor(generics.ListAPIView):
    serializer_class = LibroSerializer

    def get(self, request, Nombre):
        libros = Libro.objects.filter(
            Q(Id_Autor_Nombre_icontains=Nombre) | 
            Q(Id_Autor_Apellido_icontains=Nombre)
        )

        if not libros.exists():
            raise NotFound("No se encontró un libro de ese autor")
        
        serializer = LibroSerializer(libros, many=True)
        return Response({
            'success': True,
            'detail': 'Libros encontrados',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


