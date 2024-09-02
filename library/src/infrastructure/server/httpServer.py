from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
from author_controllers import get_authors, insert_authors  # Certifique-se de que o caminho está correto

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == '/authors':
            get_authors(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == '/authors':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            author = json.loads(post_data)
            insert_authors(self, author['name'], author['birthdate'])
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

def create_server(port=3000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    return httpd

if __name__ == '__main__':
    server = create_server()
    print(f"Server running on port {server.server_port}")
    server.serve_forever()



# CRIANDO UM SERVIDOR HTTP com AS ROTAS