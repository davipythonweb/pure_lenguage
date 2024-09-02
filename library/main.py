import os
from pathlib import Path
from .src.infrastructure.config import load_env  # Certifique-se de que o arquivo load_env.py está no caminho correto

# Carrega as variáveis de ambiente a partir do arquivo app.conf
config_path = Path(__file__).resolve().parent.parent / '.env'
load_env(config_path)

from src.infrastructure.server.httpServer import create_server # Certifique-se de que o arquivo http_server.py está no caminho correto

# Cria o servidor HTTP
server = create_server()

# Obtém a porta do ambiente ou usa 7500 por padrão
port = int(os.getenv('PORT', 7500))

# Inicia o servidor
if __name__ == '__main__':
    print(f"Server running on port {port}")
    server.run(port=port)



# PARA RODAR SERVIDOR NA PORTA 7500