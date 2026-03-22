#!/bin/bash
set -e

echo "--- Preparando ambiente ---"
# Cria o arquivo de log se não existir e dá permissão de escrita
touch monitor.log && chmod 666 monitor.log

echo "--- Passo 1: Construindo a Imagem Docker ---"
docker compose build

echo "--- Passo 2: Subindo o Container ---"
docker compose up -d

echo "--- Passo 3: Exibindo Logs em Tempo Real ---"
docker compose logs -f