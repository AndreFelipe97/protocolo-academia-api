from rest_framework import viewsets
from .models import (
    Protocolo,
    DivisaoTreino,
    Exercicio,
    TreinoExercicio,
    Cardio
)
from .serializers import (
    ProtocoloSerializer,
    DivisaoTreinoSerializer,
    ExercicioSerializer,
    TreinoExercicioSerializer,
    CardioSerializer
)


class ProtocoloViewSet(viewsets.ModelViewSet):
    queryset = Protocolo.objects.all()
    serializer_class = ProtocoloSerializer


class DivisaoTreinoViewSet(viewsets.ModelViewSet):
    queryset = DivisaoTreino.objects.all()
    serializer_class = DivisaoTreinoSerializer


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer


class TreinoExercicioViewSet(viewsets.ModelViewSet):
    queryset = TreinoExercicio.objects.all()
    serializer_class = TreinoExercicioSerializer


class CardioViewSet(viewsets.ModelViewSet):
    queryset = Cardio.objects.all()
    serializer_class = CardioSerializer
