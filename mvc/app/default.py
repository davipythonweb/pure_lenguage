
from datetime import date, datetime
import json

from http.server import BaseHTTPRequestHandler
import psycopg2

from models import CONN_STRING



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


def insert_authors(author_data):
    """Insere um novo autor na tabela 'Authors'."""
    query = 'INSERT INTO "Authors" (name, birthdate) VALUES (%s, %s) RETURNING id'
    try:
        with psycopg2.connect(CONN_STRING) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (author_data['name'], author_data['birthdate']))
                author_id = cursor.fetchone()[0]
                conn.commit()
        
        response = {'status': 'success', 'author_id': author_id}
        print("Autor inserido com sucesso.")
        return json.dumps(response)
    except psycopg2.Error as e:
        print("Erro ao inserir autor:", str(e))
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

    def do_POST(self):
        if self.path == '/authors':
            # Ler o comprimento do conteúdo e os dados enviados no corpo da requisição
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            author_data = json.loads(post_data)
            
            # Chamar a função insert_authors e obter a resposta JSON
            response = insert_authors(author_data)
            
            # Enviar resposta HTTP
            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            # Responder para outras rotas
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Rota nao encontrada")
