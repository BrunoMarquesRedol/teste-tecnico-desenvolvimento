# Design de Dashboard: Monitoramento de Servidores Web

Este documento descreve a estratégia de monitoramento para uma infraestrutura de servidores web, utilizando a integração Zabbix + Grafana.

---

## 1. Painéis Incluídos (Métricas Chave)
* **Disponibilidade (Uptime):** Indicador visual se o host está respondendo.
* **Recursos de Sistema:** Uso de CPU (%), Memória RAM (GB) e Espaço em Disco.
* **Performance da Aplicação:** Tempo de resposta (ms) e conexões ativas.
* **Tráfego de Rede:** Bandwidth de entrada (Inbound) e saída (Outbound).

## 2. Métricas e Tipos de Gráficos
| Métrica | Tipo de Gráfico | Justificativa |
| :--- | :--- | :--- |
| **Status do Servidor** | **Stat (Texto/Cor)** | Visualização binária imediata (Online/Offline). |
| **Carga de CPU/RAM** | **Time Series** | Essencial para identificar padrões de uso e picos de tráfego. |
| **Uso de Disco** | **Gauge** | Ótimo para visualizar proximidade de limites críticos (ex: 90%). |
| **Status HTTP (2xx, 4xx, 5xx)** | **Bar Chart** | Comparação rápida de erros versus sucessos nas requisições. |

## 3. Alertas Configurados
* **Crítico (SLA):** Host inacessível por mais de 2 minutos.
* **Performance:** Uso de CPU acima de 85% por um período de 5 minutos.
* **Capacidade:** Disco com menos de 10% de espaço livre (evitar crash de log).
* **Segurança:** Pico anômalo de conexões simultâneas (possível ataque/sobrecarga).

## 4. Organização Visual
* **Topo (Header):** Cards de resumo com números grandes (Total de Erros, Uptime Atual).
* **Corpo (Main):** Gráficos de linha (Time Series) ocupando a largura total para análise histórica.
* **Lateral/Rodapé:** Tabela de eventos/problemas ativos vindos diretamente do Zabbix.

## 5. Variáveis para Filtros
* `$host`: Permite alternar o dashboard inteiro entre diferentes servidores web.
* `$interface`: Filtra métricas de rede para placas específicas (eth0, lo, etc).
* `$time_range`: Variável nativa do Grafana para análise de períodos (5m, 1h, 24h).