"""Modelos do app de tarefas."""

from django.db import models
from django.utils import timezone

PRIORIDADES = [
    ("low", "Baixa"),
    ("medium", "Média"),
    ("high", "Alta"),
    ("urgent", "Urgente"),
]

CATEGORIAS = [
    ("estudos", "Estudos"),
    ("trabalho", "Trabalho"),
    ("pessoal", "Pessoal"),
    ("saude", "Saúde"),
    ("outros", "Outros"),
]


class Tarefa(models.Model):
    """Representa uma tarefa."""

    titulo = models.CharField("Título", max_length=200)
    descricao = models.TextField("Descrição", blank=True)
    prioridade = models.CharField(
        "Prioridade",
        max_length=10,
        choices=PRIORIDADES,
        default="medium",
    )
    categoria = models.CharField(
        "Categoria",
        max_length=20,
        choices=CATEGORIAS,
        default="outros",
    )
    concluida = models.BooleanField("Concluída", default=False)
    data_vencimento = models.DateField("Data de Vencimento", null=True, blank=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        ordering = ["-prioridade", "-criado_em"]
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return f"{self.titulo} — {'Concluída' if self.concluida else 'Pendente'}"

    def esta_atrasada(self):
        if self.data_vencimento and not self.concluida:
            return self.data_vencimento < timezone.now().date()
        return False

    def dias_para_vencer(self):
        if self.data_vencimento and not self.concluida:
            return (self.data_vencimento - timezone.now().date()).days
        return None