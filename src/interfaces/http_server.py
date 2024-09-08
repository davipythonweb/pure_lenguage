
from http.server import HTTPServer, BaseHTTPRequestHandler
from src.presentation.controllers.author_controller import AuthorController

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """class para chamar as funcoes dos controllers"""
    def do_GET(self):
        """requisicoes via get"""
        if self.path.startswith('/authors/'):
            author_id = int(self.path.split('/')[-1])
            response = AuthorController.get_author_by_id(self, author_id)
            self.send_response(response['status'])
            self.end_headers()
            self.wfile.write(json.dumps(response['data']).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """chama o controller para o server"""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Running server on port 8000...')
    httpd.serve_forever()
