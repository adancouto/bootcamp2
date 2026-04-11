"""Configuração do admin para o app de tarefas."""

from django.contrib import admin

from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ["titulo", "prioridade", "categoria", "concluida", "data_vencimento", "criado_em"]
    list_filter = ["prioridade", "categoria", "concluida", "data_vencimento"]
    search_fields = ["titulo", "descricao"]
    date_hierarchy = "criado_em"
    readonly_fields = ["criado_em"]