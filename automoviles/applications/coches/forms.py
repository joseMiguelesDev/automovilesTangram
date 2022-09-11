from django import forms
from django.utils.html import strip_tags

# Modelos
from .models import Marca, Modelo, Coche


# Formulario para registrar marcas
class FormularioMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre', 'logo')
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder':'Indique marca de automóvil...',
                    'id':'id_nombre',
                    'class':'form-control'
                }
            )
        }
    
    # Validamos el campo
    def clean_nombre(self):
        # Limpiamos el campo de etiquetas html y espacios en blanco adicionales
        nombre = str.strip(strip_tags(self.cleaned_data['nombre']))
        
        # Validamos
        if nombre is None:
            raise forms.ValidationError('Debe indicar un nombre de marca')
        
        # Retornamos el valor
        return nombre
    
    
# Formulario para registrar modelos
class FormularioModelo(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ('marca','nombre',)
        widgets = {
            'marca': forms.Select(
                attrs={
                    'id':'id_marca',
                    'class':'form-select'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder':'Indique modelo del automóvil...',
                    'id':'id_modelo',
                    'class':'form-control'
                }
            )
        }
        
    # Validamos el campo
    def clean_nombre(self):
        # Limpiamos el campo de etiquetas html y espacios en blanco adicionales
        nombre = str.strip(strip_tags(self.cleaned_data['nombre']))
        
        # Validamos
        if nombre is None:
            raise forms.ValidationError('Debe indicar un nombre de marca')
        
        # Retornamos el valor
        return nombre
    
    
# Formulario para registrar automóviles
class FormularioAutomovil(forms.ModelForm):
    class Meta:
        model = Coche
        fields = ('fecha_creacion', 'marca', 'modelo', 'imagen')
        widgets = {
            'fecha_creacion': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'placeholder':'dd/mm/yyyy',
                    'id':'id_fecha',
                    'class':'form-control'
                }
            ),
            'marca': forms.Select(
                attrs={
                    'id':'id_marca',
                    'class':'form-select'
                }
            ),
            'modelo': forms.Select(
                attrs={
                    'placeholder':'Indique modelo del automóvil...',
                    'id':'id_modelo',
                    'class':'form-select'
                }
            ),
        }
