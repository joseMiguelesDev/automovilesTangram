from django.db import models
from model_utils.models import TimeStampedModel

# Managers
from .managers import ManagerAutomovil

''' MODELO => MARCA DE COCHE '''
class Marca(TimeStampedModel):
    # Campos
    nombre = models.CharField('Marca', max_length=35, unique=True)
    logo = models.ImageField('Logo', blank=True, upload_to='imgs')
    
    # Meta
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        
    def __str__(self):
        return self.nombre
    
    

''' MODELO => MODELO DE COCHE '''
class Modelo(TimeStampedModel):
    # Campos
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=35)
    
    # Metas
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        unique_together = [['marca', 'nombre']]
        
    def __str__(self):
        return self.nombre
    
    

''' MODELO => COCHE '''
class Coche(TimeStampedModel):
    # Campos
    fecha_creacion = models.DateField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='marca')
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='modelo')
    imagen = models.ImageField('Imagen', upload_to='imgs', blank=True)
    portada = models.BooleanField(default=False)
    
    # Manager
    objects = ManagerAutomovil()
    
    # Metas
    class Meta:
        verbose_name = 'Coche'
        verbose_name_plural = 'Coches'
        unique_together = [['fecha_creacion', 'marca', 'modelo']]
        
    def __str__(self):
        return self.marca.nombre + ' ' + self.modelo.nombre + ' con fecha de creación ' + str(self.fecha_creacion)
    
        
    
