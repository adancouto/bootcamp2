"""Views do app de tarefas."""

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import TarefaForm
from .models import CATEGORIAS, PRIORIDADES, Tarefa
from .services import obter_citacao_motivacional


def index(request):
    """Lista todas as tarefas com filtros avançados."""
    tarefas = Tarefa.objects.all()

    # Filtros
    prioridade_filtro = request.GET.get("prioridade", "")
    categoria_filtro = request.GET.get("categoria", "")
    status_filtro = request.GET.get("status", "")

    if prioridade_filtro:
        tarefas = tarefas.filter(prioridade=prioridade_filtro)
    if categoria_filtro:
        tarefas = tarefas.filter(categoria=categoria_filtro)
    if status_filtro == "concluidas":
        tarefas = tarefas.filter(concluida=True)
    elif status_filtro == "pendentes":
        tarefas = tarefas.filter(concluida=False)
    elif status_filtro == "atrasadas":
        tarefas = tarefas.filter(concluida=False, data_vencimento__lt=timezone.now().date())

    # Estatísticas
    total_tarefas = Tarefa.objects.count()
    tarefas_concluidas = Tarefa.objects.filter(concluida=True).count()
    tarefas_pendentes = total_tarefas - tarefas_concluidas
    tarefas_atrasadas = Tarefa.objects.filter(concluida=False, data_vencimento__lt=timezone.now().date()).count()

    progresso = (tarefas_concluidas / total_tarefas * 100) if total_tarefas > 0 else 0

    # Resumo por prioridade
    resumo_prioridade = []
    for cod, nome in PRIORIDADES:
        subtotal = Tarefa.objects.filter(prioridade=cod).count()
        if subtotal > 0:
            resumo_prioridade.append({"nome": nome, "total": subtotal, "codigo": cod})

    # Resumo por categoria
    resumo_categoria = []
    for cod, nome in CATEGORIAS:
        subtotal = Tarefa.objects.filter(categoria=cod).count()
        if subtotal > 0:
            resumo_categoria.append({"nome": nome, "total": subtotal, "codigo": cod})

    citacao = obter_citacao_motivacional()

    context = {
        "tarefas": tarefas,
        "total_tarefas": total_tarefas,
        "tarefas_concluidas": tarefas_concluidas,
        "tarefas_pendentes": tarefas_pendentes,
        "tarefas_atrasadas": tarefas_atrasadas,
        "progresso": progresso,
        "resumo_prioridade": resumo_prioridade,
        "resumo_categoria": resumo_categoria,
        "prioridades": PRIORIDADES,
        "categorias": CATEGORIAS,
        "prioridade_filtro": prioridade_filtro,
        "categoria_filtro": categoria_filtro,
        "status_filtro": status_filtro,
        "citacao": citacao,
    }
    return render(request, "tarefas/index.html", context)


def adicionar(request):
    """Adiciona uma nova tarefa."""
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa adicionada com sucesso!")
            return redirect("tarefas:index")
    else:
        form = TarefaForm()

    return render(request, "tarefas/tarefa_form.html", {"form": form, "titulo": "Adicionar Tarefa"})


def editar(request, pk):
    """Edita uma tarefa existente."""
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa atualizada com sucesso!")
            return redirect("tarefas:index")
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, "tarefas/tarefa_form.html", {"form": form, "titulo": "Editar Tarefa"})


def excluir(request, pk):
    """Exclui uma tarefa."""
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == "POST":
        tarefa.delete()
        messages.success(request, "Tarefa removida com sucesso!")
        return redirect("tarefas:index")

    return render(request, "tarefas/confirmar_exclusao.html", {"tarefa": tarefa})


def concluir(request, pk):
    """Conclui uma tarefa."""
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.concluida = True
    tarefa.save()
    messages.success(request, "Tarefa concluída com sucesso!")
    return redirect("tarefas:index")