from rest_framework import viewsets
from rest_framework.response import Response
#
from django.shortcuts import get_object_or_404

# Modelos
from .models import *

# Serializers
from .serializers import (
    AutomovilSerializer, 
    SaveAutomovilSerializer,
    ModeloSerializer
)
''' ------------------------------------------
            VIEWSET PARA MODELO 
------------------------------------------- '''
class ModeloAPI(viewsets.ViewSet):
    # Query
    modelos = Modelo.objects.all()
    
    # Listado de modelos
    def list(self, request, *args, **kwargs):
        queryset = Modelo.objects.all()
        info_serializada = ModeloSerializer(queryset, many=True)
        return Response(info_serializada.data)


 
''' ------------------------------------------
            VIEWSET PARA COCHE 
------------------------------------------- ''' 
class AutomovilAPI(viewsets.ViewSet):
    # Query
    queryset = Coche.objects.all()
    
    # Listar todos los vehículos
    def list(self, request, *args, **kwargs):
        queryset = Coche.objects.all()
        info_serializada = AutomovilSerializer(queryset, many=True)
        return Response(info_serializada.data)


    # Crear registros
    def create(self, request):
        # Deserializamos la información enviada desde el cliente
        info_deserializada = SaveAutomovilSerializer(data=request.data)
        
        # Comprobamos que los datos son los especificados en el serializador
        info_deserializada.is_valid(raise_exception=True)
        
        # Creamos el automovil
        coche = Coche.objects.create(
            fecha_creacion = info_deserializada.validated_data['fecha'],
            marca = Marca.objects.get(nombre=info_deserializada.validated_data['marca']),
            modelo = Modelo.objects.get(nombre=info_deserializada.validated_data['modelo'])
        )
        
        # Guardamos el registro
        coche.save()
        
        # Retornamos código ok
        return Response({
            'Código':'200 ok'
        })
        
    
    # Función de recuperación de registro
    def retrieve(self, request, pk=None):
        # Recuperamos el objeto
        coche = get_object_or_404(Coche.objects.all(), pk=pk)
        
        # Serializamos la información
        serializer = AutomovilSerializer(coche)
        
        # Retornamos el json
        return Response(serializer.data)
    
    
    # Función para actualizar datos 
    def update(self, request, pk=None):
        # Recuperamos el registro
        coche = get_object_or_404(Coche.objects.all(), pk=pk)
        
        # Deserializamos la información
        info_deserializada = SaveAutomovilSerializer(data=request.data)
        
        # COmprobamos que la información recibida sea válida
        info_deserializada.is_valid(raise_exception=True)
        
        # Actualizamos los datos
        coche.fecha_creacion = info_deserializada.validated_data['fecha']
        
        # Guardamos el registro
        coche.save()
        
        # Retornamos código 
        return Response({
            'Código':'200 ok'
        })
        
        
    # Borrado de registro
    def destroy(self, request, pk=None):
        # Recuperamos el registro
        coche = get_object_or_404(Coche.objects.all(), pk=pk)
        
        # Borramos el registro
        coche.delete()
        
        # Retornamos código 
        return Response({
            'Código':'200 ok'
        })
        
        