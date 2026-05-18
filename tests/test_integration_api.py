import pytest
from django.urls import reverse

from tarefas import services


class MockResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


def test_obter_citacao_motivacional_retornando_texto_e_autor(monkeypatch):
    fake_payload = {
        "content": "Progresso diário é sucesso acumulado.",
        "author": "Bootcamp API",
    }
    monkeypatch.setattr(services.requests, "get", lambda *args, **kwargs: MockResponse(fake_payload))

    resultado = services.obter_citacao_motivacional()

    assert resultado["texto"] == fake_payload["content"]
    assert resultado["autor"] == fake_payload["author"]


@pytest.mark.django_db
def test_index_exibe_citacao_motivacional(client, monkeypatch):
    fake_payload = {
        "content": "Conclua uma tarefa e celebre o progresso.",
        "author": "TaskFlow",
    }
    monkeypatch.setattr(services.requests, "get", lambda *args, **kwargs: MockResponse(fake_payload))

    response = client.get(reverse("tarefas:index"))
    html = response.content.decode()

    assert response.status_code == 200
    assert fake_payload["content"] in html
    assert fake_payload["author"] in html
