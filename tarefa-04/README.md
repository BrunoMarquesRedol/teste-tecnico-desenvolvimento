# Tarefa 04 - Containerização de Monitor de URLs

Este projeto consiste na containerização do monitor de disponibilidade desenvolvido na Tarefa 03, utilizando Docker e Docker Compose para garantir isolamento, portabilidade e persistência de dados.

## Como Executar

Para facilitar o processo de build e execução, utilize o script de automação:

1. Garanta que o script tenha permissão de execução:
   ```bash
   chmod +x run.sh

    Execute o script:
    Bash

    ./run.sh

O script run.sh irá:

    Preparar o ambiente (limpeza de containers órfãos e garantia do arquivo de log).

    Construir a imagem Docker otimizada.

    Iniciar o container em modo desacoplado (-d).

    Exibir os logs em tempo real para validação da coleta.

Diferenciais Técnicos Implementados
1. Segurança e Otimização (Dockerfile)

    Usuário Não-Root: O container utiliza o usuário bruno_user, seguindo boas práticas de segurança (Least Privilege).

    Imagem Slim: Uso da imagem python:3.12-slim para reduzir o footprint e a superfície de ataque.

    Python Unbuffered: Configurado para garantir que os logs sejam transmitidos instantaneamente para o host sem delay de buffer.

2. Persistência e Configuração (Volumes)

    Hot Reload de Configuração: O arquivo config.yaml é montado via volume, permitindo alterar URLs sem reiniciar o container.

    Logs Persistentes: O arquivo monitor.log é mapeado do container para o host, permitindo auditoria externa em tempo real via tail -f.

3. Automação e Resiliência

    Script de Orquestração: O run.sh automatiza o ciclo de vida do container.

    Variáveis de Ambiente: Configurações de log e ambiente injetadas via docker-compose.yml.

Estrutura de Arquivos

    monitor.py: Aplicação principal com múltiplos handlers de log.

    Dockerfile: Receita da imagem otimizada.

    docker-compose.yml: Orquestração de volumes, redes e ambiente.

    run.sh: Automação de processos Bash.

    config.yaml: Configurações de alvos e intervalos.