from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Ola mundo! Este eh um servidor em python.")
HTTPServer(('', 8000), Handler).serve_forever(print("rodando na porta: 8000",))
