import requests
import time
import yaml
import logging
import sys

# Configuração de Logging Estruturado (Requisito: Log em arquivo e console)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("monitor.log"), # Salva resultados com timestamp no arquivo
        logging.StreamHandler(sys.stdout)   # Exibe no console em tempo real
    ]
)

def load_config():
    """Lê as configurações do arquivo externo YAML."""
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def check_url(url, max_retries, timeout):
    """Verifica o status HTTP com implementação de Retry e Backoff Exponencial."""
    retries = 0
    backoff = 1  # Inicia o intervalo em 1 segundo
    
    while retries <= max_retries:
        try:
            start_time = time.time()
            # Verifica status HTTP e tempo de resposta
            response = requests.get(url, timeout=timeout)
            response_time = round(time.time() - start_time, 3)
            
            if response.status_code == 200:
                logging.info(f"SUCESSO: {url} | Status: {response.status_code} | Tempo: {response_time}s")
                return
            else:
                logging.warning(f"ERRO HTTP: {url} | Status: {response.status_code} | Tentativa: {retries+1}")
        
        # Tratamento específico para erros (Timeout, DNS, Conexão)
        except requests.exceptions.RequestException as e:
            logging.error(f"FALHA em {url}: {str(e)} | Tentativa: {retries+1}")

        retries += 1
        # Implementação do Backoff Exponencial: 1s, 2s, 4s (máximo 3 tentativas)
        if retries <= max_retries:
            logging.info(f"Aguardando {backoff}s para nova tentativa em {url}...")
            time.sleep(backoff)
            backoff *= 2  # Dobra o tempo a cada falha

def main():
    # Carrega configurações do arquivo YAML
    config = load_config()
    urls = config.get('urls', [])
    max_retries = config.get('max_retries', 3)
    timeout = config.get('timeout', 10)

    logging.info("Iniciando monitoramento de URLs...")
    for url in urls:
        check_url(url, max_retries, timeout)
    logging.info("Monitoramento finalizado.")

if __name__ == "__main__":
    main()