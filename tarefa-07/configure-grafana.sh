#!/bin/bash

# Cores para o log
GREEN='\033[0;32m'
NC='\033[0m' 

echo -e "${GREEN}Aguardando Grafana ficar disponível (porta 3000)...${NC}"

# Aguarda o healthcheck do Grafana
until $(curl --output /dev/null --silent --head --fail http://localhost:3000/api/health); do
    printf '.'
    sleep 2
done

echo -e "\n${GREEN}Grafana Online!${NC}"

echo "Verificando se o plugin Zabbix foi instalado pelo Docker..."
# Lista plugins instalados via API do Grafana
PLUGINS=$(curl -s -u admin:admin http://localhost:3000/api/plugins)

if echo "$PLUGINS" | grep -q "alexanderzobnin-zabbix-app"; then
    echo -e "${GREEN}Plugin Zabbix encontrado e ativo!${NC}"
else
    echo "Erro: Plugin Zabbix não encontrado. Verifique as variáveis de ambiente no docker-compose."
    exit 1
fi

echo "Testando conexão com o Datasource Zabbix..."
# Verifica se o provisionamento criou o datasource
DS_CHECK=$(curl -s -u admin:admin http://localhost:3000/api/datasources/name/Zabbix)

if [[ $DS_CHECK == *"\"name\":\"Zabbix\""* ]]; then
    echo -e "${GREEN}Datasource 'Zabbix' configurado com sucesso via Provisioning!${NC}"
else
    echo "Erro: Datasource não encontrado. Verifique o volume de provisioning."
    exit 1
fi

echo "--- Status da Configuração: OK ---"