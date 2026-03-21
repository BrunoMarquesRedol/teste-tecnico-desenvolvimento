import requests
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Configuração de Logging para substituição do print()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class UserCollector:
    """
    Classe responsável por coletar e filtrar dados de usuários de uma API REST.
    """

    def __init__(self, api_url: str, city_filter: str = None):
        """
        Inicializa o coletor com a URL da API e o filtro de cidade opcional.
        :param api_url: URL da API pública.
        :param city_filter: Nome da cidade para filtragem automática.
        """
        self.api_url = api_url
        self.city_filter = city_filter
        self.users: List[Dict] = []

    def fetch_users(self) -> List[Dict]:
        """
        Consome a API e retorna a lista bruta de usuários com tratamento de erros.
        """
        try:
            logging.info(f"Iniciando coleta de dados em: {self.api_url}")
            response = requests.get(self.api_url, timeout=10)
            
            # Validação do Status HTTP
            response.raise_for_status()
            
            self.users = response.json()
            logging.info(f"Sucesso! {len(self.users)} usuários obtidos da API.")
            return self.users

        except requests.exceptions.RequestException as err:
            logging.error(f"Erro crítico na requisição: {err}")
            return []

    def filter_by_city(self, users_list: List[Dict]) -> List[Dict]:
        """
        Filtra uma lista de usuários pela cidade especificada no __init__.
        """
        if not users_list:
            logging.warning("Lista de usuários vazia para filtragem.")
            return []
        
        # Filtra usando o critério definido na instância (city_filter)
        filtered = [
            user for user in users_list 
            if user.get('address', {}).get('city') == self.city_filter
        ]
        
        logging.info(f"Filtro aplicado para '{self.city_filter}': {len(filtered)} encontrado(s).")
        return filtered

    def generate_stats(self, filtered_users: List[Dict]) -> Dict:
        """
        Calcula estatísticas (total e lista de empresas) dos usuários filtrados.
        """
        companies = [user.get('company', {}).get('name') for user in filtered_users]
        
        stats = {
            "total_users": len(filtered_users),
            "companies_list": companies,
            "timestamp": datetime.now().isoformat()
        }
        return stats

    def save_results(self, data: List[Dict], stats: Dict, filename: str = "output.json"):
        """
        Salva o resultado e as estatísticas em um arquivo JSON estruturado.
        """
        output = {
            "metadata": stats,
            "results": data
        }
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=4, ensure_ascii=False)
            logging.info(f"Dados salvos com sucesso no arquivo: {filename}")
        except IOError as e:
            logging.error(f"Erro de E/S ao salvar o arquivo JSON: {e}")

if __name__ == "__main__":
    
    # 1. Instanciação com parâmetros
    collector = UserCollector(
        api_url='https://jsonplaceholder.typicode.com/users',
        city_filter='South Christy'
    )
    
    # 2. Coleta de dados
    users = collector.fetch_users()
    
    # 3. Filtragem
    filtered = collector.filter_by_city(users)
    
    # 4. Geração de Estatísticas
    stats = collector.generate_stats(filtered)
    
    # 5. Persistência dos resultados
    collector.save_results(filtered, stats)