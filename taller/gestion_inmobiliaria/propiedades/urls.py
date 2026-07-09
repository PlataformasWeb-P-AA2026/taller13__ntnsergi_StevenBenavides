from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'edificios', views.EdificioViewSet, basename='edificio')
router.register(r'departamentos', views.DepartamentoViewSet, basename='departamento')

urlpatterns = [
    path('', views.index, name='index'),
    path('edificios/', views.listar_edificios, name='listar_edificios'),
    path('departamentos/', views.listar_departamentos, name='listar_departamentos'),
    # URLs para la API
    path('api/', include(router.urls)),
]