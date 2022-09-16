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
    ModeloSerializer,
    SaveModelo,
    MarcaSerializer,
    SaveMarca
)


''' ------------------------------------------
            VIEWSET PARA MARCA 
------------------------------------------- '''
class MarcaAPI(viewsets.ViewSet):
    # Query
    queryset = Marca.objects.all()
    
    # Listado de modelos
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        info_serializada = MarcaSerializer(queryset, many=True)
        return Response(info_serializada.data)


    # Crear modelo nuevo
    def create(self, request):
        # Obtenemos la información y la deserializamos
        info_deserializada = SaveMarca(data=request.data)
        
        # Comprobamos validez de los datos
        info_deserializada.is_valid(raise_exception=True)
        
        # Creamos el modelo
        marca = Marca.objects.create(
            nombre=info_deserializada.validated_data['nombre'],
        )
        
        # Guardamos registro
        marca.save()
        
        # Retornamos código ok
        return Response({
            'Código':'200 ok'
        })
        
    
    # Función de recuperación de registro
    def retrieve(self, request, pk=None):
        # Recuperamos el objeto
        marca = get_object_or_404(Marca.objects.all(), pk=pk)
        
        # Serializamos la información
        serializer = MarcaSerializer(marca)
        
        # Retornamos el json
        return Response(serializer.data)
        
        
    # Función para actualizar datos 
    def update(self, request, pk=None):
        # Recuperamos el registro
        marca = get_object_or_404(Marca.objects.all(), pk=pk)
        
        # Deserializamos la información
        info_deserializada = SaveMarca(data=request.data)
        
        # COmprobamos que la información recibida sea válida
        info_deserializada.is_valid(raise_exception=True)
        
        # Actualizamos los datos
        marca.nombre = info_deserializada.validated_data['nombre']
        
        # Guardamos el registro
        marca.save()
        
        # Retornamos código 
        return Response({
            'Código':'200 ok'
        })
        
        
    # Borrado de registro
    def destroy(self, request, pk=None):
        # Recuperamos el registro
        marca = get_object_or_404(Marca.objects.all(), pk=pk)
        
        # Borramos el registro
        marca.delete()
        
        # Retornamos código 
        return Response({
            'Código':'200 ok'
        })
        
        
        
''' ------------------------------------------
            VIEWSET PARA MODELO 
------------------------------------------- '''
class ModeloAPI(viewsets.ViewSet):
    # Query
    queryset = Modelo.objects.all()
    
    # Listado de modelos
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        info_serializada = ModeloSerializer(queryset, many=True)
        return Response(info_serializada.data)


    # Crear modelo nuevo
    def create(self, request):
        # Obtenemos la información y la deserializamos
        info_deserializada = SaveModelo(data=request.data)
        
        # Comprobamos validez de los datos
        info_deserializada.is_valid(raise_exception=True)
        
        # Creamos el modelo
        modelo = Modelo.objects.create(
            marca=Marca.objects.get(nombre=info_deserializada.validated_data['marca']),
            nombre=info_deserializada.validated_data['nombre']
        )
        
        # Guardamos registro
        modelo.save()
        
        # Retornamos código ok
        return Response({
            'Código':'200 ok'
        })
        
    
    # Función de recuperación de registro
    def retrieve(self, request, pk=None):
        # Recuperamos el objeto
        modelo = get_object_or_404(Modelo.objects.all(), pk=pk)
        
        # Serializamos la información
        serializer = ModeloSerializer(modelo)
        
        # Retornamos el json
        return Response(serializer.data)
        
        
    # Función para actualizar datos 
    def update(self, request, pk=None):
        # Recuperamos el registro
        modelo = get_object_or_404(Modelo.objects.all(), pk=pk)
        
        # Deserializamos la información
        info_deserializada = SaveModelo(data=request.data)
        
        # COmprobamos que la información recibida sea válida
        info_deserializada.is_valid(raise_exception=True)
        
        # Actualizamos los datos
        modelo.nombre = info_deserializada.validated_data['nombre']
        modelo.marca = Marca.objects.get(nombre=info_deserializada.validated_data['marca'])
        
        # Guardamos el registro
        modelo.save()
        
        # Retornamos código 
        return Response({
            'Código':'200 ok'
        })
        
        
    # Borrado de registro
    def destroy(self, request, pk=None):
        # Recuperamos el registro
        modelo = get_object_or_404(Modelo.objects.all(), pk=pk)
        
        # Borramos el registro
        modelo.delete()
        
        # Retornamos código 
        return Response({
            'Código':'200 ok'
        })
 
''' ------------------------------------------
            VIEWSET PARA COCHE 
------------------------------------------- ''' 
class AutomovilAPI(viewsets.ViewSet):
    # Query
    queryset = Coche.objects.all()
    
    # Listar todos los vehículos
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
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
        
        