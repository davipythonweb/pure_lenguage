# criar servidor python

from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Ola mundo! Este eh um servidor em python.")
HTTPServer(('', 8000), Handler).serve_forever(print("rodando na porta: 8000",))





# import http.server
# import socketserver

# PORT = 7250

# class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         # Envia uma resposta de status 200 (OK).
#         self.send_response(200)
#         self.send_header("Content-Type", "text/html")
#         self.end_headers()
#         self.wfile.write(b"Ola mundo! Este eh um servidor em python.")

# with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
#     print(f"Servidor na porta {PORT}")
#     httpd.serve_forever()


# import http.server  # Importa o módulo para funcionalidades básicas para criar servidores HTTP.
# import socketserver  # Importa o módulo para criar servidores baseados em sockets.

# # Define a porta na qual o servidor irá escutar.
# PORT = 7250

# # Cria uma classe que herda de SimpleHTTPRequestHandler para lidar com requisições HTTP.
# class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
#     # Método para tratar requisições GET.
#     def do_GET(self):
#         # Envia uma resposta de status 200 (OK).
#         self.send_response(200)
#         # Adiciona um cabeçalho HTTP indicando o tipo de conteúdo como HTML.
#         self.send_header("Content-Type", "text/html")
#         # Finaliza os cabeçalhos da resposta.
#         self.end_headers()
#         # Escreve "Ola mundo! Este eh um servidor em python." no corpo da resposta HTTP.
#         self.wfile.write(b"Ola mundo! Este eh um servidor em python.")

# # Cria o servidor TCP que escuta na porta especificada e usa a classe SimpleHTTPRequestHandler para lidar com as requisições.
# with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
#     # Imprime uma mensagem no console indicando que o servidor está rodando na porta especificada.
#     print(f"Servidor na porta {PORT}")
#     # Mantém o servidor rodando indefinidamente, servindo as requisições que chegarem.
#     httpd.serve_forever()


# from http.server import HTTPServer, BaseHTTPRequestHandler

# # Define uma classe Handler que herda de BaseHTTPRequestHandler para lidar com requisições HTTP.
# class Handler(BaseHTTPRequestHandler):
#     # Método para tratar requisições GET.
#     def do_GET(self):
#         # Envia uma resposta de status 200 (OK).
#         self.send_response(200)
#         # Envia os cabeçalhos HTTP para indicar o fim da parte de cabeçalhos.
#         self.end_headers()
#         # Escreve "Ola, mundo!" no corpo da resposta HTTP.
#         self.wfile.write(b"Ola, mundo!")

# # Cria um servidor HTTP,na porta 8000 chama a classe Handler para as requisições.
# HTTPServer(('', 8000), Handler).serve_forever(print("rodando na porta: 8000",))
# # Mantém o servidor rodando indefinidamente, servindo as requisições que chegarem.
