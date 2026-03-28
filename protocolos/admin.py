from django.contrib import admin
from .models import (
    Protocolo,
    DivisaoTreino,
    Exercicio,
    TreinoExercicio,
    Cardio
)


# 🔗 Inline de exercícios dentro da divisão
class TreinoExercicioInline(admin.TabularInline):
    model = TreinoExercicio
    extra = 1
    ordering = ("ordem",)


# 🔗 Inline de divisões dentro do protocolo
class DivisaoTreinoInline(admin.TabularInline):
    model = DivisaoTreino
    extra = 1


# 🔗 Inline de cardio dentro do protocolo
class CardioInline(admin.StackedInline):
    model = Cardio
    extra = 0
    max_num = 1


# 📦 Admin do Protocolo (tela principal)
@admin.register(Protocolo)
class ProtocoloAdmin(admin.ModelAdmin):
    list_display = ("nome", "criado_em")
    search_fields = ("nome",)
    inlines = [DivisaoTreinoInline, CardioInline]


# 📦 Admin da Divisão
@admin.register(DivisaoTreino)
class DivisaoTreinoAdmin(admin.ModelAdmin):
    list_display = ("nome", "grupo_muscular", "protocolo")
    list_filter = ("protocolo",)
    inlines = [TreinoExercicioInline]


# 📦 Admin do Exercício (catálogo)
@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


# 📦 Admin do TreinoExercicio
@admin.register(TreinoExercicio)
class TreinoExercicioAdmin(admin.ModelAdmin):
    list_display = (
        "exercicio",
        "divisao",
        "series",
        "repeticoes_min",
        "repeticoes_max",
        "tempo_execucao",
        "ordem"
    )
    list_filter = ("divisao",)
    ordering = ("divisao", "ordem")


# 📦 Admin do Cardio
@admin.register(Cardio)
class CardioAdmin(admin.ModelAdmin):
    list_display = ("protocolo", "tempo_min", "tempo_max", "frequencia")
