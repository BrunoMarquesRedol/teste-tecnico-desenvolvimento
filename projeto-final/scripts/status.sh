#!/bin/bash
echo "--- Status da Stack de Monitoramento ---"
docker compose -f ../stack/docker-compose.yml ps
echo -e "\n--- Status do Coletor ---"
docker stats api-collector --no-stream