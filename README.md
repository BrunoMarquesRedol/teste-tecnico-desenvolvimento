# NOME: Bruno Marques  
Objetivo: Demonstrar competencias avancadas em Python, Docker, Automacao e Monitoramento de Infraestrutura.

---

## Visao Geral do Projeto
Este repositorio contem a resolucao de um teste tecnico integrado, focando em escalabilidade, resiliencia e automacao de processos. Cada tarefa foi desenvolvida com Programacao Orientada a Objetos (POO) e as melhores práticas de Clean Code (PEP 8).

## Estrutura de Diretorios
* tarefa-01/: Coletor de API REST resiliente.
* tarefa-02/: Processador de metricas e gerador de relatorios.
* tarefa-03/: Coletor robusto com Logging estruturado e Backoff Exponencial.
* tarefa-04/: Containerizacao da solucao utilizando Docker Compose.
* tarefa-05/: Deploy de Stack de Monitoramento (Zabbix + Banco de Dados) via Docker.
* tarefa-06/: Integracao Python com Zabbix API para relatorios de inventario.
* tarefa-07/: Automacao de provisionamento e integracao Grafana + Zabbix.
* projeto-final/: Solução completa end-to-end com scripts de controle.

---

## Detalhes Tecnicos em Destaque

### Automacao e Monitoramento (Tarefa 05, 06 e 07)
* **Provisionamento Declarativo (Tarefa 07):** Implementacao de Infrastructure as Code (IaC) para configurar automaticamente o Datasource do Zabbix no Grafana via arquivos de provisioning, eliminando configuracoes manuais.
* **Script de Validacao Bash:** Desenvolvimento de script para healthcheck de servicos, verificacao de plugins e teste de conectividade de API em tempo de boot.
* **Integracao JSON-RPC:** Desenvolvimento de cliente Python customizado para interacao com a API do Zabbix, respeitando protocolos de autenticacao e sessao.
* **Geracao de Relatorios:** Transformacao de payloads JSON complexos em relatorios HTML5 profissionais para tomada de decisao.

### Resiliencia e Observabilidade (Tarefa 03)
* **Estrategia de Retry:** Configuracao de ate 3 tentativas automaticas para mitigar falhas intermitentes de rede.
* **Backoff Exponencial:** Implementacao de intervalos crescentes para respeitar limites do servidor.
* **Logging Estruturado:** Saida dupla (console e arquivo) com timestamps e niveis de severidade.

### Containerizacao e DevOps (Tarefa 04)
* **Seguranca (Non-Root):** Dockerfile configurado para execucao com usuario comum, mitigando riscos de privilegios elevados.
* **Persistencia:** Uso de volumes gerenciados para logs, banco de dados (PostgreSQL) e configuracoes de dashboards.

---

## Como Executar
1. Certifique-se de possuir Docker e Docker Compose instalados.
2. Na pasta \`projeto-final/scripts\`, execute: \`./init.sh\`.
3. Para monitorar o status, use: \`./status.sh\`.

## Pre-requisitos
* Python 3.12 ou superior.
* Docker e Docker Compose (versao atualizada).
* Git (para versionamento).

## Uso de Inteligencia Artificial
Conforme permitido nas instrucoes, utilizei ferramentas de IA (Gemini) para:
* Refinamento da documentacao tecnica e revisao de Clean Code.
* Otimizacao de handlers de log e estrutura de classes para integracao com API.

## Fontes de Pesquisa
* Documentacao Oficial Python 3.12+
* Zabbix API Documentation (JSON-RPC 2.0)
* Grafana Provisioning Documentation
* Docker Documentation (Volumes & Security Best Practices)

---
*Bruno Marques - Marco de 2026*
EOF