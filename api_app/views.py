from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics , status
from rest_framework.exceptions import NotFound
from .serializers import AutorSerializer,TareaSerializer
from .models import Autor,Tarea
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
        Biografia=request.data.get('Biografia',None)

        #Verificar si la biografia ha cambiado
        if Biografia and Biografia != Autor.email:
            serializer=AutorSerializer(Autor, data=request.data)

#Eliminar Autor

