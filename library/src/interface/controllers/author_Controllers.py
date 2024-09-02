from http.server import BaseHTTPRequestHandler
import json
from src.core.usecases.author_Use_Cases import get_authors_use_case, insert_authors_use_case

def get_authors(handler: BaseHTTPRequestHandler):
    try:
        authors = get_authors_use_case()
        handler.send_response(200)
        handler.send_header('Content-Type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps(authors).encode())
    except Exception as err:
        handler.send_response(500)
        handler.send_header('Content-Type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps({'error': 'Internal Server Error'}).encode())

def insert_authors(handler: BaseHTTPRequestHandler, name: str, birthdate: str):
    try:
        author = insert_authors_use_case(name, birthdate)
        handler.send_response(201)
        handler.send_header('Content-Type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps(author).encode())
    except Exception as err:
        handler.send_response(500)
        handler.send_header('Content-Type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps({'error': 'Internal Server Error'}).encode())


# CREATE CONTROLLERS

# FUNÇÂO PARA PEGAR getAuthors
# FUNÇÂO PARA INSERRIR insertAuthors

