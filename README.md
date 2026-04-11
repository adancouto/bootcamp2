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

# Autor
Adan Couto — github.com/adancouto

# Repositório
github.com/adancouto/bootcamp2
