"""URLs do app de tarefas."""

from django.urls import path

from . import views

app_name = "tarefas"

urlpatterns = [
    path("", views.index, name="index"),
    path("adicionar/", views.adicionar, name="adicionar"),
    path("editar/<int:pk>/", views.editar, name="editar"),
    path("excluir/<int:pk>/", views.excluir, name="excluir"),
    path("concluir/<int:pk>/", views.concluir, name="concluir"),
]