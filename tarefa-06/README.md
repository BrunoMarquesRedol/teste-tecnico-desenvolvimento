# Tarefa 06 - Integracao Python + Zabbix API

Este projeto utiliza Python para automatizar a extracao de dados do Zabbix via chamadas JSON-RPC 2.0, focando em inventario de ativos e monitoramento de incidentes.

## Funcionalidades
* Autenticacao segura via API (Session Token).
* Listagem de hosts e interfaces de rede.
* Extracao de problemas (triggers) em estado de alerta.
* Geracao de relatorio consolidado em HTML5/CSS3 (Dashboard Estatico).

## Estrutura de Arquivos
* zabbix_client.py: Cliente JSON-RPC para comunicacao com o servidor.
* report_generator.py: Motor de transformacao de dados para HTML.
* main.py: Script orquestrador do fluxo de execucao.

## Como Executar
1. Certifique-se que a infraestrutura da Tarefa 05 (Docker) esta operacional.
2. Instale as dependencias: `pip install -r requirements.txt`
3. Configure as variaveis de ambiente para evitar hardcoding de senhas:
   ```bash
   export ZABBIX_URL="http://localhost:8080"
   export ZABBIX_USER="Admin"
   export ZABBIX_PASS="zabbix"