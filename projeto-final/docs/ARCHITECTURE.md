# Arquitetura Técnica

[Coletor Python] --(HTTP GET)--> [APIs Públicas]
      |
      | (Geração de Logs/Métricas)
      v
[Zabbix Server] <--(Monitorização)--> [PostgreSQL]
      |
      +--> [Grafana Dashboard] (Visualização Final)