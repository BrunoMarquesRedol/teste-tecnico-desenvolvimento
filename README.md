# Teste Técnico - Monitoramento de APIs e Automação
NOME: Bruno Marques  
Objetivo: Demonstrar competências avançadas em Python, Docker, Automação e Monitoramento.

---

## Visão Geral do Projeto
Este repositório contém a resolução de um teste técnico integrado, focando em escalabilidade, resiliência e automação de processos. Cada tarefa foi desenvolvida seguindo o paradigma de Programação Orientada a Objetos (POO) e as melhores práticas de Clean Code (PEP 8).

## Estrutura de Diretórios
* tarefa-01/: Coletor de API REST resiliente.
* tarefa-02/: Processador de métricas e gerador de relatórios.
* tarefa-03/: Coletor robusto com Logging estruturado e Backoff Exponencial.
* tarefa-04/: Containerização completa da solução utilizando Docker Compose e volumes persistentes para logs e configurações.

---

## Detalhes Técnicos em Destaque

### Resiliência e Observabilidade (Tarefa 03)
* Estratégia de Retry: Configuração de até 3 tentativas automáticas para mitigar falhas intermitentes de rede.
* Backoff Exponencial: Implementação de intervalos crescentes (1s, 2s, 4s) para respeitar os limites do servidor e evitar bloqueios.
* Logging Estruturado: Saída dupla (console e arquivo monitor.log) com timestamps e níveis de severidade para auditoria.

### Containerização e DevOps (Tarefa 04)
* Segurança (Non-Root): Dockerfile configurado para rodar com o usuário bruno_user, evitando privilégios de administrador no container.
* Persistência via Volumes: Sincronização em tempo real do arquivo de log e suporte a hot-reload de configurações via config.yaml.
* Otimização: Uso de imagens python:3.12-slim e modo PYTHONUNBUFFERED para logs instantâneos.

---

## Pré-requisitos
Para executar este projeto, você precisará de:
* Python 3.12 ou superior.
* Docker e Docker Compose (versão atualizada).
* Git (para versionamento).

## Uso de Inteligência Artificial
Conforme permitido nas instruções do teste, utilizei ferramentas de IA (Gemini) para:
* Refinamento da estrutura de documentação técnica.
* Otimização de handlers de log para ambiente containerizado.
* Revisão de lógica para tratamento de exceções robusto e Backoff Exponencial.

## Fontes de Pesquisa
* Documentação Oficial Python 3.12+
* Biblioteca Requests - Guia do Usuário
* Docker Documentation (Volumes & Security Best Practices)
* Repositório de APIs Públicas (JSONPlaceholder / PokeAPI)

---

## Como Navegar
Cada pasta possui seu próprio README.md com instruções específicas de execução e detalhes técnicos individuais. Por favor, acesse as subpastas para validar os resultados de cada etapa.