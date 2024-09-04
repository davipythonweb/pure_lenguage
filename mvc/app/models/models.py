# carregando variaveis de ambiente
# conexao ao banco postgres
# query no banco na tabela authors
# funcao que cria servidor e faz um request na rota localhost:8000/authors

import os
import json
from datetime import date, datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import psycopg2
from dotenv import load_dotenv # pylint: disable=import-error

# Carregar variáveis de ambiente do arquivo .env
load_dotenv('../../.env')

# Obter variáveis de configuração
conn_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'host': os.getenv('DB_HOST'),
    'password': os.getenv('DB_PASS'),
    'port': os.getenv('DB_PORT', '5432')
}

# Criar string de conexão
CONN_STRING = ' '.join([f"{key}='{value}'" for key, value in conn_params.items()])

def get_authors():
    """Consulta a tabela 'Authors' e retorna todos os detalhes dos autores em formato JSON."""
    query = 'SELECT * FROM "Authors"'  # Usar aspas duplas para referenciar a tabela
    try:
        with psycopg2.connect(CONN_STRING) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                authors = cursor.fetchall()
                colnames = [desc[0] for desc in cursor.description]
                
        # Formatar resposta em JSON, convertendo `date` para string
        response = {
            'count': len(authors),
            'authors': [
                {
                    colname: (value.isoformat() if isinstance(value, (date, datetime)) else value)
                    for colname, value in zip(colnames, row)
                } for row in authors
            ]
        }
        print("Query executada com sucesso, retornando dados.")
        return json.dumps(response)
    except psycopg2.Error as e:
        print("Erro ao conectar ou executar a query:", str(e))
        return json.dumps({'error': str(e)})
        

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/authors':
            # Chamar a função get_authors e obter a resposta JSON
            response = get_authors()
            
            # Enviar resposta HTTP
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            # Responder para outras rotas
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Rota nao encontrada")

# Configurar e iniciar o servidor
server_address = ('', 8000)
httpd = HTTPServer(server_address, Handler)
print("Rodando na porta: 8000")
httpd.serve_forever()
