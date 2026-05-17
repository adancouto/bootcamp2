"""Serviços externos do app de tarefas."""

import requests

API_CITACAO = "https://api.quotable.io/random"


def obter_citacao_motivacional():
    """Busca uma citação motivacional em uma API pública."""
    try:
        response = requests.get(API_CITACAO, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "texto": data.get("content", "Acredite no poder de um dia bem planejado."),
            "autor": data.get("author", "Autor Desconhecido"),
        }
    except requests.RequestException:
        return {
            "texto": "Acredite no poder de um dia bem planejado.",
            "autor": "TaskFlow",
        }
