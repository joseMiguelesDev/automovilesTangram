from rest_framework.routers import DefaultRouter
from . import viewsets

# Registramos las urls
router = DefaultRouter()
router.register(r'automoviles', viewsets.AutomovilAPI, basename='automoviles')
router.register(r'modelos', viewsets.ModeloAPI, basename='modelos')
router.register(r'marcas', viewsets.MarcaAPI, basename='marcas')

# Patterns url
urlpatterns = router.urls