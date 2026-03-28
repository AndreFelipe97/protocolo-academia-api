from django.db import models


class Protocolo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class DivisaoTreino(models.Model):
    protocolo = models.ForeignKey(
        Protocolo,
        on_delete=models.CASCADE,
        related_name="divisoes"
    )
    nome = models.CharField(max_length=2)  # A, B, C, D...
    grupo_muscular = models.CharField(max_length=100)

    class Meta:
        unique_together = ("protocolo", "nome")
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.grupo_muscular}"


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class TreinoExercicio(models.Model):
    TIPO_EXECUCAO_CHOICES = [
        ("reps", "Repetições"),
        ("tempo", "Tempo"),
    ]

    divisao = models.ForeignKey(
        DivisaoTreino,
        on_delete=models.CASCADE,
        related_name="exercicios"
    )
    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE
    )

    series = models.IntegerField()

    # Para exercícios por repetição (ex: 8 a 10)
    repeticoes_min = models.IntegerField(null=True, blank=True)
    repeticoes_max = models.IntegerField(null=True, blank=True)

    # Para exercícios por tempo (ex: prancha 30s)
    tempo_execucao = models.IntegerField(
        null=True,
        blank=True,
        help_text="Tempo em segundos"
    )

    tipo_execucao = models.CharField(
        max_length=10,
        choices=TIPO_EXECUCAO_CHOICES,
        default="reps"
    )

    carga = models.FloatField(null=True, blank=True)
    tempo_descanso = models.IntegerField(
        null=True,
        blank=True,
        help_text="Tempo de descanso em segundos"
    )

    ordem = models.IntegerField()

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        if self.tipo_execucao == "tempo":
            return f"{self.exercicio.nome} ({self.series}x {self.tempo_execucao}s)"
        return f"{self.exercicio.nome} ({self.series}x {self.repeticoes_min}-{self.repeticoes_max})"


class Cardio(models.Model):
    protocolo = models.OneToOneField(
        Protocolo,
        on_delete=models.CASCADE,
        related_name="cardio"
    )

    tempo_min = models.IntegerField(default=10)
    tempo_max = models.IntegerField(default=40)
    frequencia = models.CharField(
        max_length=100,
        default="Todos os dias"
    )

    def __str__(self):
        return f"Cardio {self.tempo_min}-{self.tempo_max} min"
