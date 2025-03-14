# Projeto de Classificação Financeira

Este projeto é uma aplicação de classificação de categorias financeiras usando FastAPI. Ele utiliza um modelo de classificação logística treinado e um CountVectorizer para transformar os dados de entrada.

## Estrutura do Projeto

- `financial_category_model/main.py`: Contém a aplicação FastAPI que recebe entradas de lançamentos financeiros e retorna suas classificações.

## Requisitos

Certifique-se de ter todas as bibliotecas necessárias instaladas. Você pode instalar os requisitos usando o arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Como Executar


2. A aplicação FastAPI estará disponível e você pode enviar requisições POST para o endpoint `/greet/` com o seguinte formato:

```json
{
  "lancamentos": ["descrição do lançamento 1", "descrição do lançamento 2"]
}
```

## Exemplo de Uso

Envie uma requisição POST para `http://0.0.0.0:5757/greet/` com o corpo JSON:

```json
{
  "lancamentos": ["compra no supermercado", "pagamento de aluguel"]
}
```

A resposta será algo como:

```json
{
  "classifications": ["categoria_supermercado", "categoria_aluguel"]
}
```

## Estrutura dos Modelos

Os modelos treinados (`count_vectorizer.pkl` e `logistic_classifier.pkl`) devem estar localizados no diretório `model/`.

