Tarefa 01: Coletor de API REST (Arquitetura POO)
Objetivo

Desenvolver um script automatizado em Python para consumir dados da API pública JSONPlaceholder, realizar filtragem segmentada por localização e gerar um relatório de métricas estruturado.
Tecnologias Utilizadas

    Python 3.9+

    Requests: Para consumo da API REST via HTTP.

    Logging: Para rastreabilidade de execução e substituição do print.

    JSON & Datetime: Para persistência de dados e geração de timestamps.

Como Executar

    Acesse o diretório da tarefa no terminal:
    Bash

cd tarefa-01

Instale as dependências necessárias:
Bash

pip install -r requirements.txt

Execute o coletor:
Bash

    python3 collector.py

Exemplo de Uso Interno

O script segue rigorosamente o padrão de chamada programática esperado:
Python

collector = UserCollector(
    api_url='https://jsonplaceholder.typicode.com/users',
    city_filter='South Christy'
)
users = collector.fetch_users()
filtered = collector.filter_by_city(users)
stats = collector.generate_stats(filtered)
collector.save_results(filtered, stats)

Exemplo de Saída (output.json)

O script gera um arquivo JSON estruturado contendo metadados de execução e os resultados filtrados:
JSON

{
    "metadata": {
        "total_users": 1,
        "companies_list": [
            "Romaguera-Jacobson"
        ],
        "timestamp": "2026-03-21T18:45:00.000000"
    },
    "results": [
        {
            "id": 1,
            "name": "Leanne Graham",
            "address": {
                "city": "South Christy"
            },
            "company": {
                "name": "Romaguera-Jacobson"
            }
        }
    ]
}