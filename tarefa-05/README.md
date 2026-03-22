# Tarefa 05 - Stack de Monitoramento (Zabbix + Grafana)

Este projeto implementa uma stack completa de monitoramento containerizada, utilizando Docker Compose para orquestrar serviços de banco de dados, servidor de monitoramento, interface web e dashboards.

## Arquitetura da Stack
* **PostgreSQL 15 (Alpine)**: Banco de dados relacional para persistência do Zabbix.
* **Zabbix Server 6.0 LTS**: Core de monitoramento para coleta de dados.
* **Zabbix Web (Nginx)**: Interface de gerenciamento acessível na porta 8080.
* **Grafana**: Ferramenta de visualização de dados na porta 3000, pré-configurada com o plugin oficial do Zabbix.

## Como Iniciar

O ambiente é automatizado via scripts Bash:

1.  **Subir a Stack**:
    ```bash
    ./setup.sh
    ```
    *O script verifica dependências, gera o arquivo `.env` e aguarda o healthcheck do banco de dados.*

2.  **Acesso**:
    * **Zabbix**: `http://localhost:8080` (Admin / zabbix)
    * **Grafana**: `http://localhost:3000` (admin / admin)

3.  **Remover a Stack**:
    ```bash
    ./teardown.sh
    ```

## Diferenciais Técnicos
* **Healthchecks**: O Zabbix Server e o Frontend utilizam condições de `service_healthy` para garantir que o PostgreSQL esteja pronto para conexões antes de iniciarem, evitando falhas de boot.
* **Segurança e Isolamento**: Utilização de uma rede Docker dedicada (`monitor-net`) e isolamento do banco de dados, que não expõe portas para o host externo.
* **Persistência**: Volumes nomeados garantem que os dados do monitoramento e dashboards do Grafana não sejam perdidos em reinicializações.
* **Automação Resiliente**: O script `setup.sh` utiliza `set -e` para interromper a execução em caso de erros e garante a idempotência do arquivo de configuração.