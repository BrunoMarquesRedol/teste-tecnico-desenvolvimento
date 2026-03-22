#!/bin/bash

# set -e: Para o script se algo der errado
set -e

echo "----------------------------------------------------"
echo "   Finalizando Stack de Monitoramento (T05)         "
echo "----------------------------------------------------"

# 1. Verifica se o docker-compose.yml existe na pasta
if [ ! -f docker-compose.yml ]; then
    echo "ERRO: Arquivo docker-compose.yml não encontrado nesta pasta."
    exit 1
fi

# 2. Para os containers e remove volumes/redes
echo "[1/2] Parando containers e removendo volumes..."
# O parâmetro -v remove os volumes nomeados (pg_data, grafana_data)
# O parâmetro --remove-orphans limpa containers antigos que sobraram
docker compose down -v --remove-orphans

# 3. Limpeza de logs (Opcional, mas profissional)
echo "[2/2] Limpando arquivos temporários..."
# Se você quiser manter o .env, não apague ele aqui.
# Mas se quiser um reset total, pode descomentar a linha abaixo:
# rm -f .env

echo "----------------------------------------------------"
echo " Ambiente limpo com sucesso!"
echo "----------------------------------------------------"