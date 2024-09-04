# importar variaveis de ambiente
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv('../../.env')

# Obter e armazenar as variáveis em variáveis Python
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Imprimir os valores das variáveis
print(f"DB_USER: {db_user}")
print(f"DB_PASS: {db_pass}")
print(f"DB_HOST: {db_host}")
print(f"DB_PORT: {db_port}")
print(f"DB_NAME: {db_name}")

# conexao com banco postgres
