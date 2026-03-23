# Tarefa 07: Automacao Grafana + Zabbix

Este modulo automatiza a integracao entre o Grafana e o Zabbix, eliminando a necessidade de configuracao manual via interface Web.

## O que foi implementado:
1. Provisioning Engine: Utilizacao do motor de provisionamento do Grafana para criar o Datasource Zabbix no boot.
2. Plugin Automation: Instalacao dinamica do plugin alexanderzobnin-zabbix-app via Docker.
3. Validation Script: Script Bash que aguarda o healthcheck da API e valida a integridade do plugin e do datasource.
4. Dashboard Design: Documentacao tecnica descrevendo a arquitetura de um dashboard de alta performance.

## Como Validar
1. Certifique-se de que a stack da tarefa-05 esta rodando.
2. Execute o script de validacao:
   ./configure-grafana.sh
3. Acesse http://localhost:3000 (admin/admin) e verifique em Data Sources que o Zabbix ja esta conectado.

## Estrutura de Arquivos
* docs/dashboard-design.md: Planejamento das metricas e paineis.
* grafana/provisioning/datasources/zabbix.yml: Configuracao declarativa do datasource.
* configure-grafana.sh: Script de automacao e teste.
