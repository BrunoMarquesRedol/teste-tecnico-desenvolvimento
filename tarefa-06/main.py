import os
import logging
from zabbix_client import ZabbixAPI
from report_generator import HTMLReportGenerator

# Configura o logging: essencial para monitorar o comportamento do script sem poluir o output principal
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    """
    Função principal que coordena o fluxo de automação:
    1. Carregamento de credenciais via Variáveis de Ambiente.
    2. Autenticação (Login) no Servidor Zabbix.
    3. Coleta de dados (Hosts e Problemas).
    4. Processamento e Geração do Relatório HTML.
    """
    
    # 1. CONFIGURAÇÕES DE ACESSO
    # Prioriza variáveis de ambiente por segurança (evita hardcoding de senhas)
    url  = os.getenv("ZABBIX_URL", "http://localhost:8080")
    user = os.getenv("ZABBIX_USER", "Admin")
    pw   = os.getenv("ZABBIX_PASS", "zabbix")

    # Inicializa a instância da nossa classe de API
    client = ZabbixAPI(url, user, pw)
    
    logging.info(f"Iniciando tentativa de conexao em: {url}")
    
    # 2. FLUXO DE AUTENTICAÇÃO
    # O método login() retorna True se o token de sessão for obtido com sucesso
    if client.login():
        
        # 3. COLETA DE DADOS (READ OPERATIONS)
        logging.info("Coletando inventario de hosts e alertas ativos...")
        hosts = client.get_hosts()
        problems = client.get_problems()
        
        # 4. VALIDAÇÃO E GERAÇÃO DO RELATÓRIO
        # Verificamos se as listas não são nulas (o que indicaria erro na chamada da API)
        if hosts is not None and problems is not None:
            
            # Chama o gerador estático de HTML
            report_file = HTMLReportGenerator.generate(hosts, problems)
            
            if report_file:
                # Exibe mensagem de sucesso limpa, sem emojis, focada na localização do arquivo
                print("\n" + "="*50)
                print("RELATORIO GERADO COM SUCESSO!")
                print(f"Diretorio: {os.path.abspath(report_file)}")
                print("="*50 + "\n")
            else:
                logging.error("Falha ao gravar o arquivo de relatorio em disco.")
        else:
            logging.error("Falha na extracao de dados: Resposta da API inconsistente.")
    else:
        logging.error("Erro de autenticacao: Verifique URL, usuario e senha.")

if __name__ == "__main__":
    # Ponto de entrada garantido do script
    main()