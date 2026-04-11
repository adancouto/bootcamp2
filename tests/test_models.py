import pytest
from tarefas.models import Tarefa

@pytest.mark.django_db
def test_criar_tarefa():
    """Testa a criação de uma tarefa."""
    tarefa = Tarefa.objects.create(
        descricao="Estudar Python",
        prioridade="high",
    )
    assert tarefa.pk is not None
    assert tarefa.descricao == "Estudar Python"
    assert tarefa.prioridade == "high"
    assert tarefa.concluida is False

@pytest.mark.django_db
def test_str_tarefa():
    """Testa a representação em string de uma tarefa."""
    tarefa = Tarefa(titulo="Fazer compras", descricao="Ir ao supermercado")
    assert str(tarefa) == "Fazer compras — Pendente"

@pytest.mark.django_db
def test_listagem_tarefas():
    """Testa a listagem de tarefas."""
    Tarefa.objects.create(titulo="Tarefa 1", descricao="Descrição 1", prioridade="low")
    Tarefa.objects.create(titulo="Tarefa 2", descricao="Descrição 2", prioridade="medium")

    tarefas = Tarefa.objects.all()
    assert tarefas.count() == 2
