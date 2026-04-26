# Banco de Dados e Big Data

Aplicação prática de tecnologias de Banco de Dados e Big Data em uma empresa de comércio eletrônico.

Autora: Sonia Avila

---

## Tecnologias Utilizadas

- Python  
- Streamlit  
- MongoDB  
- Docker  
- Docker Compose  
- Pandas  

---

## Funcionalidades

- Cadastro de usuários (nome e e-mail)  
- Visualização dos dados em tabela  
- Edição e exclusão de registros  
- Integração com banco de dados MongoDB  
- Execução via Docker  

### Análise de Dados

A aplicação possui uma funcionalidade de análise básica de dados, exibindo o total de registros cadastrados em tempo real.

Essa métrica permite uma visualização rápida do volume de dados armazenados, demonstrando na prática conceitos relacionados a Big Data.

---

## Estrutura do Projeto


📁 projeto-python
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt


---

## Sobre a aplicação

A aplicação permite cadastrar, visualizar, editar e excluir dados armazenados no MongoDB, utilizando uma interface simples desenvolvida com Streamlit.

---

## Segurança e Boas Práticas

Embora este projeto tenha fins acadêmicos, em um ambiente real seriam necessárias medidas adicionais, como:

- Validação de dados de entrada  
- Controle de acesso de usuários  
- Proteção de dados sensíveis  
- Adequação à LGPD  

---

## Objetivo do Projeto

Demonstrar a integração entre diferentes tecnologias, abordando conceitos de desenvolvimento web, banco de dados e conteinerização de aplicações.

## Considerações Finais

Este projeto representa uma aplicação prática dos conhecimentos adquiridos, evidenciando a construção de uma aplicação funcional de forma organizada e estruturada.

---

## Como Executar

### Usando Docker Compose

```bash
docker-compose up --build

Acesse no navegador:

http://localhost:8501

## Execução alternativa (Docker)
docker build -t projetopython .
docker run -p 8501:8501 projetopython
