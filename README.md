# 🎬 Catálogo de Filmes - Django

## Sobre o Projeto

Este projeto foi desenvolvido utilizando o framework Django com o objetivo de criar um catálogo de filmes. O sistema permite cadastrar, visualizar, editar e excluir filmes armazenados em um banco de dados SQLite.

Além do CRUD completo, o sistema utiliza a API OMDb para buscar automaticamente informações dos filmes a partir do título informado pelo usuário.

## Funcionalidades

* Adicionar filmes
* Listar filmes cadastrados
* Editar informações dos filmes
* Excluir filmes
* Exibir pôster dos filmes
* Calcular a média das notas cadastradas
* Buscar informações de filmes através da API OMDb

## Tecnologias Utilizadas

* Python 3
* Django
* SQLite
* HTML5
* CSS3
* OMDb API

## Estrutura do Projeto

catalogo_filmes/

├── catalogo_filmes/

├── filmes/

│   ├── migrations/

│   ├── templates/

│   │   ├── lista_filmes.html

│   │   ├── adicionar_filme.html

│   │   └── editar_filme.html

│   ├── forms.py

│   ├── models.py

│   ├── urls.py

│   └── views.py

├── db.sqlite3

├── manage.py

└── README.md

## Como Executar

1. Clone ou baixe o projeto para seu computador.

2. Abra o terminal na pasta do projeto.

3. Instale as dependências necessárias:

   pip install django requests

4. Execute as migrações do banco de dados:

   python manage.py migrate

5. Inicie o servidor Django:

   python manage.py runserver

6. Abra o navegador e acesse:

   http://127.0.0.1:8000

## Modelo de Dados

Cada filme possui os seguintes atributos:

* Título
* Ano
* Diretor
* Gênero
* Nota
* URL do pôster

## API Utilizada

OMDb API

A API é utilizada para buscar informações de filmes a partir do título informado pelo usuário, preenchendo automaticamente os dados do cadastro.

Site oficial:

https://www.omdbapi.com/

## Autor

Projeto desenvolvido para a disciplina de Frameworks Web utilizando Django.
