Nome: Bruno

Objetivo: Demonstrar competências em Python, Docker, Automação e Monitoramento.
Visão Geral do Projeto

Este repositório contém a resolução do teste técnico integrado, focando em escalabilidade, resiliência e automação. Cada tarefa foi desenvolvida seguindo o paradigma de Programação Orientada a Objetos (POO) e as melhores práticas de Clean Code (PEP 8).
Estrutura de Diretórios

    tarefa-01/: Coletor de API REST resiliente.

    tarefa-02/: Processador de métricas e gerador de relatórios.

    tarefa-03/: Coletor robusto com Logging estruturado e Backoff Exponencial.

Detalhes Técnicos da Tarefa 03

Nesta etapa, o foco foi a implementação de resiliência em scripts de automação:

    Estratégia de Retry: Configuração de até 3 tentativas automáticas para mitigar falhas intermitentes de rede.

    Backoff Exponencial: Implementação de intervalos crescentes (1s, 2s, 4s) para respeitar os limites do servidor e evitar bloqueios.

    Observabilidade: Utilização da biblioteca logging para saída dupla (console e arquivo monitor.log) com timestamps e níveis de severidade.

    Configuração Externa: Separação de lógica e dados através de arquivos YAML, permitindo alterações de parâmetros sem modificação do código-fonte.

Pré-requisitos

Para executar qualquer parte deste projeto, você precisará de:

    Python 3.9 ou superior

    Docker e Docker Compose

    Git (para clonar o repositório)

Uso de Inteligência Artificial

Conforme permitido nas instruções do teste, utilizei ferramentas de IA (Gemini/ChatGPT) para:

    Refinamento da estrutura de documentação técnica.

    Revisão de lógica para tratamento de exceções robusto.

    Otimização de comentários e docstrings para máxima clareza.

Fontes de Pesquisa

    Documentação Oficial Python 3.10+

    Biblioteca Requests - Guia do Usuário

    Repositório de APIs Públicas (JSONPlaceholder)

Como Navegar

Cada pasta possui seu próprio README.md com instruções específicas de execução e detalhes técnicos daquela tarefa. Por favor, acesse as subpastas para validar os resultados individuais.