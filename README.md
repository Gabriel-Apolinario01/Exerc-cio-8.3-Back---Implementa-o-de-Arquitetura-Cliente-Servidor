# API Livraria - Back-end (Exercicio 8.3)

Este repositorio contem a API Back-end do sistema de livraria, desenvolvida em Python com Flask. O projeto foi refatorado para implementar a Arquitetura Cliente-Servidor, separando completamente as responsabilidades da Interface (Front-end) das regras de negocio e persistencia de dados (Back-end).

Aviso: Este e apenas o repositorio do Back-end. O Cliente (Front-end independente construido com HTML/JS) deve ser executado separadamente para consumir esta API.

## Tecnologias Utilizadas
* Python 3.x
* Flask: Microframework para criacao da API REST.
* Flask-CORS: Biblioteca utilizada para permitir as requisicoes (Cross-Origin) vindas do Front-end independente.
* Manipulacao de TXT: Persistencia de dados (historico de compras) utilizando arquivos de texto para simular um banco de dados.

## Arquitetura
O codigo foi estruturado baseando-se em principios de Clean Architecture, dividindo as camadas em:
* entities: Modelos de dados (ex: Livro).
* use_cases: Regras de negocio da aplicacao.
* interface: Controladores que intermediam a comunicacao entre as rotas da API e os Use Cases.
* infra: Repositorios responsaveis por acessar e persistir os dados (Leitura e gravacao no compras.txt).

## Como Executar o Projeto

1. Clone o repositorio:
git clone https://github.com/Gabriel-Apolinario01/Exerc-cio-8.3-Back---Implementa-o-de-Arquitetura-Cliente-Servidor.git
cd "Livraria Cliente-Servidor"

2. Instale as dependencias:
Certifique-se de ter o Python instalado. No terminal, instale o Flask e o CORS:
pip install flask flask-cors

3. Execute o Servidor:
python app.py

O servidor sera iniciado na porta 5000 (http://127.0.0.1:5000). Mantenha este terminal aberto para que o Front-end consiga consumir a API.

## Endpoints da API REST

A API retorna exclusivamente dados em formato JSON.

* GET / : Rota base de status (Verifica se a API esta online).
* GET /api/livros : Retorna a lista completa de livros disponiveis no catalogo.
* GET /api/comprar/<id> : Processa a compra de um livro com base no ID passado na URL e salva o registro no arquivo texto.
* GET /api/compras : Le o arquivo texto e retorna o historico completo de todas as compras realizadas.

---
Projeto desenvolvido para a disciplina de Engenharia de Software.
