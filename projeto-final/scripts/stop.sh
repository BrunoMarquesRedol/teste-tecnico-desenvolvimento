# start.sh
#!/bin/bash
# Inicia os containers já configurados
docker compose -f ../stack/docker-compose.yml start

# stop.sh
#!/bin/bash
# Para os containers mas mantém os volumes (dados)
docker compose -f ../stack/docker-compose.yml stop