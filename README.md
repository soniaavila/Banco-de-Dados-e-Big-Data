# Banco-de-Dados-e-Big-Data
Aplicação Prática de Tecnologias de Banco de Dados e Big Data em uma Empresa de Comércio Eletrônico

 Autora
Sonia Avila

## Tecnologias Utilizadas

- Python
- Streamlit
- MongoDB
- Docker
- Docker Compose
- Pandas

## Funcionalidades

- Inserção de dados (nome e e-mail)
- Edição e exclusão de dados
- Consulta e visualização em tabela
- Manipulação de dados com Pandas

##  Estrutura do Projeto
📁 projeto-python
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt

###  Sobre a aplicação

A aplicação permite cadastrar, visualizar, editar e excluir dados armazenados no MongoDB, utilizando uma interface simples desenvolvida com Streamlit.

### Segurança e Boas Práticas

Embora este projeto tenha fins acadêmicos, em um ambiente real seriam necessárias medidas adicionais, como:

Validação de dados de entrada
Controle de acesso de usuários
Proteção de dados sensíveis
Adequação à LGPD

### Objetivo do Projeto

Demonstrar a integração entre diferentes tecnologias, abordando conceitos de desenvolvimento web, banco de dados e conteinerização de aplicações.

### Considerações Finais

Este projeto representa uma aplicação prática dos conhecimentos adquiridos em desenvolvimento de sistemas, evidenciando a criação de uma aplicação funcional de forma organizada e estruturada.


## Como Executar

###  Usando Docker Compose

```bash
docker-compose up --build

### Acessar aplicação

Após executar, acesse no navegador:

http://localhost:8501

**Execução alternativa (Docker)**

docker build -t projetopython .
docker run -p 8501:8501 projetopython



