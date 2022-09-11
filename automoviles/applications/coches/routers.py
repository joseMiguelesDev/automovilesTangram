from rest_framework.routers import DefaultRouter
from . import viewsets

# Registramos las urls
router = DefaultRouter()
router.register(r'automoviles', viewsets.AutomovilAPI, basename='automoviles')

# Patterns url
urlpatterns = router.urls