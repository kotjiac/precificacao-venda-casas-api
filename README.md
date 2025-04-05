# API de Precificação de Casas 🏠

Este projeto transforma um modelo de regressão treinado em uma API para predição de preços de venda de casas.

## 🔧 Como executar

### Com Docker

```bash
docker build -t precificador .
docker run -p 8000:8000 precificador
```

### Localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📡 Endpoint

`POST /predict`

### Exemplo de entrada JSON:

```json
{
  "zipcode": "98074",
  "sqft_living": 1680,
  "grade": 6,
  "sqft_above": 1680,
  "sqft_living15": 1800,
  "bathrooms": 2.0
}
```

### Exemplo de resposta:

```json
{
  "predicted_price": 289000.0
}
```

## 🧪 Teste rápido

Você pode testar a API com este comando:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "zipcode": "98074",
    "sqft_living": 1680,
    "grade": 6,
    "sqft_above": 1680,
    "sqft_living15": 1800,
    "bathrooms": 2.0
}'
```

## 📁 Estrutura do projeto

- `main.py`: implementação da API
- `utils.py`: funções auxiliares
- `model.joblib`: modelo treinado
- `requirements.txt`: dependências
- `Dockerfile`: container Docker
- `README.md`: instruções de uso
- `notebook/precificacao_venda_casas.ipynb`: notebook original