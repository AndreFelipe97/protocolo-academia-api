from rest_framework import serializers
from .models import (
    Protocolo,
    DivisaoTreino,
    Exercicio,
    TreinoExercicio,
    Cardio
)


class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = "__all__"


class TreinoExercicioSerializer(serializers.ModelSerializer):
    exercicio = ExercicioSerializer(read_only=True)

    class Meta:
        model = TreinoExercicio
        fields = "__all__"


class DivisaoTreinoSerializer(serializers.ModelSerializer):
    exercicios = TreinoExercicioSerializer(many=True)

    class Meta:
        model = DivisaoTreino
        fields = "__all__"

    def create(self, validated_data):
        exercicios_data = validated_data.pop("exercicios")
        divisao = DivisaoTreino.objects.create(**validated_data)

        for exercicio_data in exercicios_data:
            TreinoExercicio.objects.create(divisao=divisao, **exercicio_data)

        return divisao


class CardioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardio
        fields = "__all__"


class ProtocoloSerializer(serializers.ModelSerializer):
    divisoes = DivisaoTreinoSerializer(many=True)
    cardio = CardioSerializer()

    class Meta:
        model = Protocolo
        fields = "__all__"

    def create(self, validated_data):
        divisoes_data = validated_data.pop("divisoes")
        cardio_data = validated_data.pop("cardio")

        protocolo = Protocolo.objects.create(**validated_data)

        # cria cardio
        Cardio.objects.create(protocolo=protocolo, **cardio_data)

        # cria divisões e exercícios
        for divisao_data in divisoes_data:
            exercicios_data = divisao_data.pop("exercicios")
            divisao = DivisaoTreino.objects.create(
                protocolo=protocolo,
                **divisao_data
            )

            for exercicio_data in exercicios_data:
                TreinoExercicio.objects.create(
                    divisao=divisao,
                    **exercicio_data
                )

        return protocolo
