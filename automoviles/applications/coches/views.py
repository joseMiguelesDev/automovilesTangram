from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Vistas genéricas
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView,
)

# Modelos
from .models import Marca, Modelo, Coche

# Formularios
from .forms import (
    FormularioMarca, 
    FormularioModelo, 
    FormularioAutomovil
)



''' --------------------------------------------------- 
                    LISTVIEWS
--------------------------------------------------- '''
# Vista para listar la página de inicio
class Home(ListView):
    template_name = 'home/home.html'
    context_object_name = 'automoviles'
    
    # Queryset que devuelve todos los vehículos que estén seleccionados para la portada
    def get_queryset(self):
        return Coche.objects.filter(
            portada=True
        )
        

# Vista para listar todas las marcas de vehículos
class ListarMarcas(ListView):
    template_name = 'automoviles/lista_marcas.html'
    context_object_name = 'marcas'
    
    # Queryset que devuelve todas las marcas
    def get_queryset(self):
        return Marca.objects.all()


# Vista para listar todos los modelos de vehículos
class ListarModelos(ListView):
    template_name = 'automoviles/lista_modelos.html'
    context_object_name = 'modelos'
    paginate_by = 5
    
    # Queryset que devuelve todos los modelos
    def get_queryset(self):
        return Modelo.objects.all() 
    
    
# Vista para listar todos los vehículos
class ListarAutomoviles(ListView):
    template_name = 'automoviles/lista_coches.html'
    context_object_name = 'automoviles'
    paginate_by = 5
    
    # Queryset que devuelve todos los vehículos y comprueba si se realizo alguna búsqueda
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        return Coche.objects.automoviles_por_marca(marca)


# Template para redenrizar el formulario de búsqueda        
def formulario_busqueda(request):
    # Renderizamos la template
    return render(request, "automoviles/formulario_busqueda.html")


def listar_automoviles_segun_datos(request):

    msg = ''
    # Si las variables recibidas son las esperadas    
    if request.GET['marca'] and request.GET['modelo']:
        # Recogemos los datos
        marca = request.GET['marca']
        modelo = request.GET['modelo']
                
        # Recuperamos los datos de la BD
        automoviles = Coche.objects.listado_coches_segun_marca_modelo(marca, modelo)
        if len(automoviles) == 0: msg = 'No existen registros'
        
        # Retornamos el resultado
        return render(request, "automoviles/formulario_busqueda.html", {'msg':msg, 'automoviles':automoviles})
    
    else:
        msg = "La información enviada al servidor no es válida"
        return render(request, "automoviles/formulario_busqueda.html", {'mensaje':msg})



''' --------------------------------------------------- 
                    CREATEVIEWS
--------------------------------------------------- '''
# Vista para registrar marcas
class RegistrarMarca(CreateView):
    template_name = 'automoviles/registrar_marca.html'
    form_class = FormularioMarca
    success_url = reverse_lazy('automoviles_app:automoviles-marca-lista')
    
    
# Vista para registrar modelos
class RegistrarModelo(CreateView):
    template_name = 'automoviles/registrar_modelo.html'
    form_class = FormularioModelo
    success_url = reverse_lazy('automoviles_app:automoviles-registrar-modelo')
    
    
# Vista para registrar automóviles
class RegistrarAutomovil(CreateView):
    template_name = 'automoviles/registrar_automovil.html'
    form_class = FormularioAutomovil
    success_url = reverse_lazy('automoviles_app:automoviles-registrar')
    
    
''' --------------------------------------------------- 
                    UPDATEVIEWS
--------------------------------------------------- '''
# Vista para actualizar marca
class ActualizarMarca(UpdateView):
    template_name = 'automoviles/actualizar_marca.html'
    model = Marca
    form_class = FormularioMarca
    success_url = reverse_lazy('automoviles_app:automoviles-marca-lista')
    
    # Función para retornar el objeto o un not found
    def get_object(self, queryset=None):
        # Pk para retornar los datos del registro a actualizar
        pk = self.kwargs.get(self.pk_url_kwarg)
        
        # Devolvemos el objeto
        return get_object_or_404(Marca, id=pk)
    
    
# Vista para actualiar los modelos
class ActualizarModelo(UpdateView):
    template_name = 'automoviles/actualizar_modelo.html'
    model = Modelo
    form_class = FormularioModelo
    success_url = reverse_lazy('automoviles_app:automoviles-modelo-lista')

    # Función para retornar el objeto o un not found
    def get_object(self, queryset=None):
        # Pk para retornar los datos del registro a actualizar
        pk = self.kwargs.get(self.pk_url_kwarg)
        
        # Devolvemos el objeto
        return get_object_or_404(Modelo, id=pk)
    
    
# Vista para actualizar los datos del automóvil
class ActualizarAutomovil(UpdateView):
    template_name = 'automoviles/actualizar_automovil.html'
    model = Coche
    form_class = FormularioAutomovil
    success_url = reverse_lazy('automoviles_app:automoviles-lista')
    
    # Función para retornar el objeto o un not found
    def get_object(self, queryset=None):
        # Pk para retornar los datos del registro a actualizar
        pk = self.kwargs.get(self.pk_url_kwarg)
        
        # Devolvemos el objeto
        return get_object_or_404(Coche, id=pk)
    
    
    
''' --------------------------------------------------- 
                    DELETEVIEWS
--------------------------------------------------- '''
# Vista para eliminar marca
class EliminarMarca(DeleteView):
    template_name = 'automoviles/eliminar_registro.html'
    model = Marca
    success_url = '/'
    
    # Función para retornar el objeto o un not found
    def get_object(self, queryset=None):
        # Pk para retornar los datos del registro a actualizar
        pk = self.kwargs.get(self.pk_url_kwarg)
        
        # Devolvemos el objeto
        return get_object_or_404(Marca, id=pk)
    
    
# Vista para eliminar modelo
class EliminarModelo(DeleteView):
    template_name = 'automoviles/eliminar_registro.html'
    model = Modelo
    success_url = '/'
    
    # Función para retornar el objeto o un not found
    def get_object(self, queryset=None):
        # Pk para retornar los datos del registro a actualizar
        pk = self.kwargs.get(self.pk_url_kwarg)
        
        # Devolvemos el objeto
        return get_object_or_404(Modelo, id=pk)
    
    
# Vista para eliminar un automóvil
class EliminarAutomovil(DeleteView):
    template_name = 'automoviles/eliminar_registro.html'
    model = Coche
    success_url = '/'
    
    # Función para retornar el objeto o un not found
    def get_object(self, queryset=None):
        # Pk para retornar los datos del registro a actualizar
        pk = self.kwargs.get(self.pk_url_kwarg)
        
        # Devolvemos el objeto
        return get_object_or_404(Coche, id=pk)

    