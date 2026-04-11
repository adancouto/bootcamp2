"""Formulários do app de tarefas."""

from django import forms
from django.utils import timezone

from .models import Tarefa


class TarefaForm(forms.ModelForm):
    """Formulário para criação e edição de tarefas."""

    class Meta:
        model = Tarefa
        fields = ["titulo", "descricao", "prioridade", "categoria", "data_vencimento"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ex: Estudar para prova de matemática"}
            ),
            "descricao": forms.Textarea(
                attrs={"class": "form-control", "rows": 3, "placeholder": "Detalhes adicionais da tarefa..."}
            ),
            "prioridade": forms.Select(attrs={"class": "form-select"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "data_vencimento": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get("titulo", "").strip()
        if not titulo:
            raise forms.ValidationError("O título não pode estar vazio.")
        return titulo

    def clean_data_vencimento(self):
        data = self.cleaned_data.get("data_vencimento")
        if data and data < timezone.now().date():
            raise forms.ValidationError("A data de vencimento não pode ser no passado.")
        return data