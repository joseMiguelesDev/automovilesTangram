from django.db import models
from django.shortcuts import get_object_or_404

# Managers para Automovil
class ManagerAutomovil(models.Manager):
    
    # Obtener un listado de automóviles por marca
    def automoviles_por_marca(self, marca):
        return self.filter(
            marca__nombre__icontains=marca
        )
    
    
    # Obtener todos los automóviles cuya fecha de creación sea anterior a una dada por parámetro
    def automoviles_por_fecha(self, fecha):
        try:
            listado = self.filter(
            fecha_creacion__lt=fecha
        ) 
        except:
            listado = []
           
        return listado
    
    
    # Obtener los automóviles por identificador por parámetro
    def automoviles_por_id(self, id):
        return get_object_or_404(self, pk=id)
        
    
    # Obtener diccionario en función de la marca
    def listado_marca_coches(self):
        listado = dict()
        for coche in self.all():
            if listado.get(coche.marca.nombre, -1) == -1:
                listado[coche.marca.nombre] = set()
            
            listado.get(coche.marca.nombre).add(coche)
            
        return listado
    
    
    # Obtener coches segun marca y modelo
    def listado_coches_segun_marca_modelo(self, marca, modelo):
        return self.filter(
            marca__nombre__icontains=marca,
            modelo__nombre__icontains=modelo
        )