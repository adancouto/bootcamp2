# 📚 Gerenciador de Tarefas Acadêmicas

## Descrição do Problema

Estudantes têm dificuldade em organizar tarefas e prazos acadêmicos, levando a atrasos e estresse desnecessário.

## Proposta de Solução

Aplicação web para gerenciar tarefas com prioridade, status de conclusão e acompanhamento de progresso.

## Público-alvo

Estudantes universitários, alunos do ensino médio e qualquer pessoa que precisa organizar tarefas diárias.

## Funcionalidades

- Listar tarefas com filtros por prioridade
- Adicionar novas tarefas
- Editar tarefas existentes
- Excluir tarefas
- Marcar tarefas como concluídas
- Visualizar progresso geral
- Resumo por prioridade

## Tecnologias Utilizadas

- Python 3.11
- Django 4.2
- SQLite
- Bootstrap 5.3
- pytest / pytest-django
- ruff

## Instalação

```bash
# Clone o repositório
git clone https://github.com/adancouto/bootcamp2.git
cd bootcamp2

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Execução

python manage.py runserver

Acesse em: http://127.0.0.1:8000

# Testes

pytest

# Lint

ruff check .

# Versão
1.0.0

# Deploy
Link público: https://<seu-deploy-aqui>

## Como publicar
- Instale as dependências: `pip install -r requirements.txt`
- Use `gunicorn` como servidor de aplicação
- Se estiver usando Render, o comando de start pode ser:

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

## Variáveis de ambiente recomendadas
- `DJANGO_DEBUG=false`
- `DJANGO_ALLOWED_HOSTS=<seu-app>.onrender.com`
- `DJANGO_SECRET_KEY=<uma-chave-secreta>`

## Deploy no Render
Se estiver usando Render, o arquivo `render.yaml` já está configurado para:
- instalar dependências
- executar as migrações com `python manage.py migrate`
- iniciar o app com `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

# Autor
Adan Couto — github.com/adancouto

# Repositório
github.com/adancouto/bootcamp2
