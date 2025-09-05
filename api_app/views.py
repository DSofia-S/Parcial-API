from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics , status
from rest_framework.exceptions import NotFound
from .serializers import AutorSerializer,EditorialSerializer,LibroSerializer,MiembroSerializer,PrestamoSerializer
from .models import Autor,Editorial,Libro,Miembro,Prestamo
from django.shortcuts import get_object_or_404

# Create your views here.

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
        Autor=get_object_or_404(Autor, pk=pk)
        serializer=AutorSerializer(Autor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail':'Autor actualizado con éxito', 'data':serializer.data}, status=status.HTTP_200_OK)

#Eliminar Autor
class EliminarAutor(generics.DestroyAPIView):
    queryset=Autor.objects.all()
    serializer_class=AutorSerializer

    def delete(self, request, pk):
        Autor=get_object_or_404(Autor, pk=pk)
        Autor.delete()
        return Response({'success':True, 'detail':'Autor eliminado con éxito'}, status=status.HTTP_200_OK)
