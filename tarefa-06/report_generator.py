import os

class HTMLReportGenerator:
    """
    Classe responsável por transformar listas de dicionários Python 
    em um documento visual formatado (Dashboard estático).
    """
    
    @staticmethod
    def generate(hosts, problems, output_file="report.html"):
        """
        Método estático para gerar o arquivo HTML.
        :param hosts: Lista retornada pelo zabbix_client
        :param problems: Lista de problemas retornada pelo zabbix_client
        """
        
        # --- Lógica de Negócio do Relatório ---
        total_hosts = len(hosts)
        # Status '0' no Zabbix significa monitorado (Ativo/Online)
        active_hosts = len([h for h in hosts if h['status'] == '0'])
        total_problems = len(problems)

        # --- Estrutura Visual (HTML5 + CSS3) ---
        html_content = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Relatório de Infraestrutura - Zabbix</title>
            <style>
                body {{ 
                    font-family: 'Segoe UI', system-ui, sans-serif; 
                    background-color: #f4f7f9; 
                    margin: 0; padding: 40px; 
                    color: #333;
                }}
                .container {{ 
                    max-width: 1100px; 
                    margin: auto; 
                    background: white;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
                }}
                h1 {{ 
                    color: #2c3e50; 
                    text-align: left; 
                    border-left: 6px solid #007bff; 
                    padding-left: 15px; 
                    margin-bottom: 30px;
                }}
                
                .summary-grid {{ 
                    display: grid; 
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
                    gap: 20px; 
                    margin: 30px 0; 
                }}
                .card {{ 
                    background: #fff; 
                    padding: 25px; 
                    border-radius: 10px; 
                    border: 1px solid #e1e4e8;
                    text-align: center;
                }}
                .card h3 {{ font-size: 14px; color: #7f8c8d; text-transform: uppercase; margin: 0; }}
                .card p {{ font-size: 36px; font-weight: 800; margin: 10px 0 0; color: #2c3e50; }}

                table {{ 
                    width: 100%; 
                    border-collapse: collapse; 
                    margin-top: 20px;
                }}
                th {{ 
                    background-color: #f8f9fa; 
                    color: #2c3e50; 
                    padding: 15px; 
                    text-align: left; 
                    border-bottom: 2px solid #dee2e6;
                }}
                td {{ 
                    padding: 15px; 
                    border-bottom: 1px solid #eee; 
                }}
                tr:hover {{ background-color: #fcfcfc; }}

                /* Status Textual */
                .status-active {{ color: #28a745; font-weight: bold; }}
                .status-inactive {{ color: #dc3545; font-weight: bold; }}

                .footer-security {{ 
                    margin-top: 50px; 
                    font-size: 12px; 
                    color: #95a5a6; 
                    text-align: center; 
                    border-top: 1px solid #eee; 
                    padding-top: 20px; 
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Monitoramento de Infraestrutura</h1>
                
                <div class="summary-grid">
                    <div class="card"><h3>Total de Ativos</h3><p>{total_hosts}</p></div>
                    <div class="card"><h3>Monitorados</h3><p>{active_hosts}</p></div>
                    <div class="card"><h3>Incidentes</h3><p style="color: {'#dc3545' if total_problems > 0 else '#2c3e50'}">{total_problems}</p></div>
                </div>

                <h2>Inventário de Hosts</h2>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Hostname</th>
                            <th>IP da Interface</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join([f'''
                        <tr>
                            <td>{h['hostid']}</td>
                            <td>{h['name']}</td>
                            <td>{h['interfaces'][0]['ip'] if h.get('interfaces') else 'N/A'}</td>
                            <td>
                                <span class="{'status-active' if h['status'] == '0' else 'status-inactive'}">
                                    {'ATIVO' if h['status'] == '0' else 'INATIVO'}
                                </span>
                            </td>
                        </tr>
                        ''' for h in hosts])}
                    </tbody>
                </table>

                <div class="footer-security">
                    <p>Relatorio gerado via Backend Python - Protocolo JSON-RPC 2.0</p>
                    <p>Segurança: Operações de escrita restritas ao ambiente de execução do script.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(html_content)
            return output_file
        except IOError as e:
            print(f"Erro ao gravar arquivo HTML: {e}")
            return None