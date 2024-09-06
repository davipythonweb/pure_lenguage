from http.server import HTTPServer

from app.controllers.default import Handler


# Configurar e iniciar o servidor
server_address = ('', 8000)
httpd = HTTPServer(server_address, Handler)
print("Rodando na porta: 8000")
httpd.serve_forever()


# APRESENTANDO ERROR:
#  "error": "could not translate host name \"None\" to address: Name or service not known\n"