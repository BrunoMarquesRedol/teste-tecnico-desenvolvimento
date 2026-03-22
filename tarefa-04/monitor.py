import requests
import time
import yaml
import logging
import os

# Configuração de Logging com dois destinos: Terminal e Arquivo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("monitor.log"),  # Gravando no arquivo persistido pelo volume
        logging.StreamHandler()             # Enviando para o stdout (docker logs)
    ]
)

def load_config():
    """Carrega as URLs do arquivo config.yaml (Volume)"""
    try:
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logging.error(f"Erro ao carregar config.yaml: {e}")
        # URLs de fallback caso o arquivo falhe
        return {
            "apis": [
                {"name": "JSONPlaceholder", "url": "https://jsonplaceholder.typicode.com/posts/1"},
                {"name": "PokeAPI", "url": "https://pokeapi.co/api/v2/pokemon/1"},
                {"name": "HTTPBin", "url": "https://httpbin.org/get"}
            ],
            "interval": 60
        }

def collect_metrics(apis):
    """Executa a coleta de disponibilidade e latência"""
    for api in apis:
        try:
            start_time = time.time()
            response = requests.get(api['url'], timeout=10)
            end_time = time.time()
            
            latency = round((end_time - start_time) * 1000, 2)
            status = response.status_code
            available = 1 if status == 200 else 0
            
            logging.info(f"API: {api['name']} | Status: {status} | Latency: {latency}ms | Avail: {available}")
            
        except Exception as e:
            logging.error(f"Erro ao coletar {api['name']}: {e}")

if __name__ == "__main__":
    logging.info("Iniciando Coletor de APIs (Containerizado)...")
    
    while True:
        # Recarrega a config em cada loop para permitir mudanças "quentes" via volume
        config = load_config()
        collect_metrics(config.get('apis', []))
        
        interval = config.get('interval', 60)
        time.sleep(interval)