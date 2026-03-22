import json
import logging
import re
import csv
from datetime import datetime
from typing import List, Dict, Any

# Configuração de Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MetricsProcessor:
    def __init__(self, cpu_threshold: int = 80, mem_threshold: int = 90):
        self.cpu_threshold = cpu_threshold
        self.mem_threshold = mem_threshold
        self.processed_data: List[Dict] = []

    def parse_metrics(self, metrics_str: str) -> Dict[str, int]:
        """Extrai métricas usando Regex: cpu:XX|mem:YY -> {'cpu': XX, 'mem': YY}"""
        pattern = r"(\w+):(\d+)"
        matches = re.findall(pattern, metrics_str)
        return {key: int(value) for key, value in matches}

    def process_data(self, input_file: str):
        """Lê o JSON e identifica servidores com problemas"""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                # Carrega a lista direta de servidores
                servers = json.load(f)
            
            for srv in servers:
                metrics = self.parse_metrics(srv.get("metrics", ""))
                
                # Regra de negócio: CPU > 80 ou Memória > 90
                has_issue = metrics.get("cpu", 0) > self.cpu_threshold or \
                            metrics.get("mem", 0) > self.mem_threshold
                
                self.processed_data.append({
                    "name": srv.get("server"),
                    "metrics": metrics,
                    "status": "CRITICAL" if has_issue else "OK",
                    "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            logging.info(f"Processamento concluído para {len(self.processed_data)} servidores.")
        except Exception as e:
            logging.error(f"Erro ao processar dados: {e}")

    def calculate_averages(self) -> Dict[str, float]:
        """Calcula a média aritmética de CPU, Memória e Disco"""
        if not self.processed_data:
            return {}
        
        totals = {"cpu": 0, "mem": 0, "disk": 0}
        count = len(self.processed_data)
        
        for item in self.processed_data:
            m = item["metrics"]
            for key in totals:
                totals[key] += m.get(key, 0)
        
        return {f"avg_{k}": round(v / count, 2) for k, v in totals.items()}

    def export_results(self, json_file: str, csv_file: str):
        """Gera os arquivos de saída nos formatos JSON e CSV"""
        if not self.processed_data:
            logging.warning("Sem dados para exportar.")
            return

        # Exportação JSON (inclui as médias calculadas)
        averages = self.calculate_averages()
        final_output = {
            "averages": averages,
            "server_reports": self.processed_data
        }
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(final_output, f, indent=4)

        # Exportação CSV
        keys = ["name", "status", "processed_at"]
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(self.processed_data)
        
        logging.info(f"Relatórios gerados: {json_file} e {csv_file}")

if __name__ == "__main__":
    processor = MetricsProcessor()
    processor.process_data("input.json")
    processor.export_results("output.json", "output.csv")