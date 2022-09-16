#
from rest_framework import serializers
from .models import Coche, Marca, Modelo


''' ------------------------------------------
            SERIALIZADOR PARA COCHE 
------------------------------------------- ''' 
class AutomovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coche
        fields = (
            'id',
            'fecha_creacion',
            'marca',
            'modelo',
            'portada',
            'imagen'
        )
        

# Serializador para crear rgistros coche
class SaveAutomovilSerializer(serializers.Serializer):
    fecha = serializers.CharField()
    marca = serializers.CharField()
    modelo = serializers.CharField()
    
    # Validamos que la marca insertada exista
    def validate_marca(self, data):      
         
        marcas = Marca.objects.filter(nombre=data)
        if len(marcas) == 0:
            raise serializers.ValidationError('La marca no existe')
        
        return data
    
    # Validamos el modelo
    def validate_modelo(self, data):        
        modelo = Modelo.objects.filter(nombre=data)
        
        if len(modelo) == 0:
            raise serializers.ValidationError('El modelo no existe')
    
        return data