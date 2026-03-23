import requests
import json
import logging

class ZabbixAPI:
    """
    Cliente para interacao com a API do Zabbix via JSON-RPC 2.0.
    Implementa autenticacao, coleta de hosts, problemas e itens de monitoramento.
    """

    def __init__(self, url, user, password):
        self.url = f"{url}/api_jsonrpc.php"
        self.user = user
        self.password = password
        self.token = None

    def login(self) -> bool:
        """
        Realiza a autenticacao no Zabbix e armazena o token de sessao.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.password
            },
            "id": 1,
            "auth": None
        }

        try:
            response = requests.post(self.url, json=payload, timeout=10)
            result = response.json()

            if "result" in result:
                self.token = result["result"]
                logging.info("Sessão iniciada com sucesso na API.")
                return True
            else:
                logging.error(f"Falha na autenticacao: {result.get('error', {}).get('data')}")
                return False
        except Exception as e:
            logging.error(f"Erro de conexao com a API: {e}")
            return False

    def get_hosts(self) -> list:
        """
        Obtem a lista de todos os hosts configurados no inventario.
        Inclui hostid, nome, status e interfaces.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["hostid", "name", "status"],
                "selectInterfaces": ["ip"]
            },
            "auth": self.token,
            "id": 2
        }

        try:
            response = requests.post(self.url, json=payload, timeout=10)
            return response.json().get("result", [])
        except Exception as e:
            logging.error(f"Erro ao buscar hosts: {e}")
            return []

    def get_problems(self) -> list:
        """
        Busca problemas (triggers) que estao atualmente em estado de alerta.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": "problem.get",
            "params": {
                "output": "extend",
                "selectAcknowledges": "extend",
                "recent": "true",
                "sortfield": ["eventid"],
                "sortorder": "DESC"
            },
            "auth": self.token,
            "id": 3
        }

        try:
            response = requests.post(self.url, json=payload, timeout=10)
            return response.json().get("result", [])
        except Exception as e:
            logging.error(f"Erro ao buscar problemas ativos: {e}")
            return []

    def get_items(self, hostid: str) -> list:
        """
        Obtem itens de monitoramento especificos de um host (Requisito 4).
        Retorna nome do item, ultimo valor e unidades.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": ["itemid", "name", "lastvalue", "units"],
                "hostids": hostid,
                "sortfield": "name"
            },
            "auth": self.token,
            "id": 4
        }

        try:
            response = requests.post(self.url, json=payload, timeout=10)
            return response.json().get("result", [])
        except Exception as e:
            logging.error(f"Erro ao buscar itens do host {hostid}: {e}")
            return []