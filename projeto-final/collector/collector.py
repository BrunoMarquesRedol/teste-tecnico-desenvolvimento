import requests
import time
import yaml
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def collect_metrics():
    apis = [
        {"name": "JSONPlaceholder", "url": "https://jsonplaceholder.typicode.com/posts/1"},
        {"name": "PokeAPI", "url": "https://pokeapi.co/api/v2/pokemon/1"},
        {"name": "HTTPBin", "url": "https://httpbin.org/get"}
    ]
    
    for api in apis:
        try:
            start_time = time.time()
            response = requests.get(api['url'], timeout=10)
            end_time = time.time()
            
            latency = round((end_time - start_time) * 1000, 2)
            status = response.status_code
            available = 1 if status == 200 else 0
            
            logging.info(f"API: {api['name']} | Status: {status} | Latency: {latency}ms | Avail: {available}")
            
            # Aqui no projeto real, você enviaria para o Zabbix via Zabbix Sender ou API
            # Para o escopo do teste, o log estruturado simula a coleta time-series
        except Exception as e:
            logging.error(f"Erro ao coletar {api['name']}: {e}")

if __name__ == "__main__":
    logging.info("Iniciando Coletor de APIs...")
    while True:
        collect_metrics()
        time.sleep(60)