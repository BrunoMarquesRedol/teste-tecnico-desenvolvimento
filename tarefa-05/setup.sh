#!/bin/bash

# set -e: Faz o script parar imediatamente se qualquer comando falhar
set -e

echo "----------------------------------------------------"
echo "  Iniciando Setup da Stack de Monitoramento (T05)   "
echo "----------------------------------------------------"

# 1. Validação de Dependências
echo "[1/4] Verificando dependências do sistema..."
if ! command -v docker &> /dev/null; then
    echo "ERRO: Docker não encontrado. Por favor, instale o Docker."
    exit 1
fi

if ! docker compose version &> /dev/null; then
    echo "ERRO: Docker Compose não encontrado ou versão antiga."
    exit 1
fi

# 2. Gestão do arquivo de configuração (.env)
echo "[2/4] Validando variáveis de ambiente..."
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        echo "Aviso: .env não encontrado. Criando a partir do .env.example..."
        cp .env.example .env
        echo "IMPORTANTE: Edite o arquivo .env com suas senhas antes de rodar em produção."
    else
        echo "ERRO Crítico: .env.example não encontrado para gerar o .env."
        exit 1
    fi
fi

# 3. Subindo a Stack
echo "[3/4] Construindo e subindo os containers..."
docker compose up -d

# 4. Aguardando Healthchecks
echo "[4/4] Aguardando serviços ficarem prontos (Healthcheck)..."
echo "Isso pode levar até 30 segundos na primeira execução..."

# Loop simples para checar se o postgres está 'healthy'
count=0
while [ "$(docker inspect -f {{.State.Health.Status}} postgres-db 2>/dev/null)" != "healthy" ]; do
    if [ $count -gt 15 ]; then
        echo "AVISO: O banco de dados está demorando mais que o esperado."
        break
    fi
    sleep 2
    ((count++))
done

echo "----------------------------------------------------"
echo "Stack de Monitoramento iniciada com sucesso!"
echo "----------------------------------------------------"
echo "Zabbix Frontend : http://localhost:8080"
echo "Grafana Dash    : http://localhost:3000"
echo "Credenciais default nos arquivos de config."
echo "----------------------------------------------------"