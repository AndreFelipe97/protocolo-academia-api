from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProtocoloViewSet,
    DivisaoTreinoViewSet,
    ExercicioViewSet,
    TreinoExercicioViewSet,
    CardioViewSet
)

router = DefaultRouter()
router.register(r'protocolos', ProtocoloViewSet)
router.register(r'divisoes', DivisaoTreinoViewSet)
router.register(r'exercicios', ExercicioViewSet)
router.register(r'treino-exercicios', TreinoExercicioViewSet)
router.register(r'cardios', CardioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
