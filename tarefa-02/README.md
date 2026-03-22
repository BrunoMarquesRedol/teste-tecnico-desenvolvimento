# Tarefa 02: Processamento de Dados (Metrics Processor)

## Objetivo
Desenvolver um script para manipulação e transformação de dados de monitoramento estruturados, convertendo strings de métricas brutas em relatórios formatados e identificando falhas críticas de infraestrutura.

## Tecnologias Utilizadas
* Python 3.9+
* Re (Regex): Para parsing de strings de métricas complexas.
* JSON & CSV: Para leitura de entradas e exportação multiformato de resultados.
* Logging: Para monitoramento do fluxo de execução e auditoria de erros.

## Como Executar
1. Acesse o diretório da tarefa no terminal:
   ```bash
   cd tarefa-02

    Execute o script:
    Bash

    python3 processor.py

    Verifique os relatórios gerados nos arquivos output.json e output.csv.

Exemplo de Entrada (input.json)
JSON

[
    {"server": "SRV-WEB-01", "metrics": "cpu:45|mem:60|disk:30"},
    {"server": "SRV-DB-01", "metrics": "cpu:92|mem:85|disk:50"},
    {"server": "SRV-APP-01", "metrics": "cpu:15|mem:40|disk:10"},
    {"server": "SRV-GW-01", "metrics": "cpu:78|mem:95|disk:20"}
]