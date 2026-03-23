NOME: Bruno Marques  
Objetivo: Demonstrar competencias avancadas em Python, Docker, Automacao e Monitoramento de Infraestrutura.

---

## Visao Geral do Projeto
Este repositorio contem a resolucao de um teste tecnico integrado, focando em escalabilidade, resiliencia e automacao de processos. Cada tarefa foi desenvolvida com Programacao Orientada a Objetos (POO) e as melhores praticas de Clean Code (PEP 8).

## Estrutura de Diretorios
* tarefa-01/: Coletor de API REST resiliente.
* tarefa-02/: Processador de metricas e gerador de relatorios.
* tarefa-03/: Coletor robusto com Logging estruturado e Backoff Exponencial.
* tarefa-04/: Containerizacao da solucao utilizando Docker Compose.
* tarefa-05/: Deploy de Stack de Monitoramento (Zabbix + Banco de Dados) via Docker.
* tarefa-06/: Integracao Python com Zabbix API para relatorios de inventario.

---

## Detalhes Tecnicos em Destaque

### Monitoramento e Infraestrutura (Tarefa 05 e 06)
* Stack Zabbix: Implementacao de ambiente de monitoramento completo utilizando Docker Compose, com persistencia de dados em volume dedicado.
* Integracao JSON-RPC: Desenvolvimento de cliente Python customizado para interacao com a API do Zabbix, respeitando protocolos de autenticacao e sessao.
* Geracao de Dashboards: Transformacao de payloads JSON complexos em relatorios HTML5 limpos e profissionais para tomada de decisao.

### Resiliencia e Observabilidade (Tarefa 03)
* Estrategia de Retry: Configuracao de ate 3 tentativas automaticas para mitigar falhas intermitentes de rede.
* Backoff Exponencial: Implementacao de intervalos crescentes para respeitar limites do servidor.
* Logging Estruturado: Saida dupla (console e arquivo) com timestamps e niveis de severidade.

### Containerizacao e DevOps (Tarefa 04)
* Seguranca (Non-Root): Dockerfile configurado para execucao com usuario comum, mitigando riscos de privilegios elevados.
* Persistencia: Uso de volumes para logs e arquivos de configuracao YAML.

---

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
* Docker Documentation (Volumes & Security Best Practices)

---
*Bruno Marques - Março de 2026*