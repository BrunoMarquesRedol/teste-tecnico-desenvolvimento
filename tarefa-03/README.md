# Tarefa 03: Monitor de URLs com Resiliência (Retry & Logging)

## Objetivo
Desenvolver um sistema de monitoramento de conectividade HTTP robusto, capaz de lidar com falhas temporárias de rede através de mecanismos de re-tentativa (retry) e backoff exponencial.

## Tecnologias Utilizadas
* Python 3.9+
* Requests: Para comunicação HTTP.
* PyYAML: Para gestão de configurações externas.
* Logging: Para registro estruturado de eventos em console e arquivo.

## Diferenciais Técnicos (Destaque +8)
* Backoff Exponencial: Implementação de algoritmo que incrementa o tempo de espera entre falhas (1s, 2s, 4s), evitando sobrecarga em serviços instáveis.
* Tratamento de Exceções Específico: Diferenciação entre Timeouts, Erros de Conexão e erros genéricos de Request para diagnósticos precisos.
* Configuração Externalizada: O comportamento do monitor (URLs, limites e retries) é controlado via arquivo YAML, seguindo princípios de Twelve-Factor App.
* Dual Logging: Registro simultâneo em console para acompanhamento em tempo real e em arquivo (`monitor.log`) para persistência de dados.

## Como Executar
1. Acesse o diretório:
   ```bash
   cd tarefa-03

    Instale as dependências:
    Bash

pip install -r requirements.txt

Execute o monitor:
Bash

    python3 monitor.py

    Verifique o histórico de logs no arquivo monitor.log.
