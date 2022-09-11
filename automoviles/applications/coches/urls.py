from django.urls import path
from . import views

# Nombre de la app
app_name = 'automoviles_app'

# Enrutado
urlpatterns = [
    # Inicio
    path(
        '',
        views.Home.as_view(),
        name='automoviles-home'
    ),
    # Listados de los modelos
    path(
        'automoviles/marca/lista/',
        views.ListarMarcas.as_view(),
        name='automoviles-marca-lista'
    ),
    path(
        'automoviles/modelo/lista/',
        views.ListarModelos.as_view(),
        name='automoviles-modelo-lista'
    ),
    path(
        'automoviles/lista/',
        views.ListarAutomoviles.as_view(),
        name='automoviles-lista'
    ),
    path(
        'automoviles/formulario-busqueda/',
        views.formulario_busqueda,
        name='automoviles-formulario'
    ),
    path(
        'buscar/',
        views.listar_automoviles_segun_datos,
        name='automoviles-resultado'
    ),
    # Registros de entradas 
    path(
        'automoviles/registrar/marca/',
        views.RegistrarMarca.as_view(),
        name='automoviles-registrar-marca'
    ),
    path(
        'automoviles/registrar/modelo/',
        views.RegistrarModelo.as_view(),
        name='automoviles-registrar-modelo'
    ),
    path(
        'automoviles/registrar/',
        views.RegistrarAutomovil.as_view(),
        name='automoviles-registrar'
    ),
    # Actualizado de los registros
    path(
        'automoviles/actualizar/marca/<int:pk>/',
        views.ActualizarMarca.as_view(),
        name='automoviles-actualizar-marca'
    ),
    path(
        'automoviles/actualizar/modelo/<pk>/',
        views.ActualizarModelo.as_view(),
        name='automoviles-actualizar-modelo'
    ),
    path(
        'automoviles/actualizar/<pk>/',
        views.ActualizarAutomovil.as_view(),
        name='automoviles-actualizar'
    ),
    # Eliminación de registros
    path(
        'automoviles/eliminar/marca/<pk>/',
        views.EliminarMarca.as_view(),
        name='automoviles-eliminar-marca'
    ),
    path(
        'automoviles/eliminar/modelo/<pk>/',
        views.EliminarModelo.as_view(),
        name='automoviles-eliminar-modelo'
    ),
    path(
        'automoviles/eliminar/<pk>',
        views.EliminarAutomovil.as_view(),
        name='automoviles-eliminar'
    ),
 
]
