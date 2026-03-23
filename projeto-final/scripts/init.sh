#!/bin/bash
# Script de inicialização completa do ambiente integrado

set -e # Aborta o script se algum comando falhar

echo " Iniciando Setup do Projeto Integrado Final..."

# 1. Criação do ficheiro .env caso não exista para evitar erros de arranque
if [ ! -f ../stack/.env ]; then
    echo " Gerando ficheiro .env padrão..."
    cat <<EOF > ../stack/.env
POSTGRES_USER=zabbix
POSTGRES_PASSWORD=zabbix_pwd
POSTGRES_DB=zabbix
ZBX_DBHOST=postgres
PHP_TZ=America/Sao_Paulo
ZABBIX_PASS=zabbix
EOF
fi

# 2. Build da imagem do Coletor Python
echo "  Construindo imagem Docker do api-collector..."
docker compose -f ../stack/docker-compose.yml build

# 3. Subida de todos os serviços em background
echo " Subindo a stack de monitorização..."
docker compose -f ../stack/docker-compose.yml up -d

echo " Ambiente pronto! Utilize ./status.sh para verificar os containers."