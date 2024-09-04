# importar variaveis de ambiente

import os
import psycopg2
from dotenv import load_dotenv # pylint: disable=import-error

# Carregar variáveis de ambiente do arquivo .env
load_dotenv('../../.env')

# pega as variaveis
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


print("------------------CONEXAO COM DATABASE--------------------------")
# conexao com banco postgres

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

# Tentar conectar ao banco de dados
try:
    with psycopg2.connect(CONN_STRING) as conn:
        print("Status: Conexão realizada com sucesso.")
except psycopg2.Error as e:
    print(f"Status: Erro na conexão. Mensagem: {e}")
finally:
    print("Tentativa de conexão finalizada.")



# conexao mais complexa

# class DatabaseConfig:
#     def __init__(self):
#         self.db_user = os.getenv('DB_USER')
#         self.db_pass = os.getenv('DB_PASS')
#         self.db_host = os.getenv('DB_HOST')
#         self.db_port = os.getenv('DB_PORT')
#         self.db_name = os.getenv('DB_NAME')
    
#     def get_connection_string(self):
#         return (f"dbname='{self.db_name}' user='{self.db_user}' "
#                 f"host='{self.db_host}' password='{self.db_pass}' port='{self.db_port}'")

# # Criar uma instância da classe DatabaseConfig
# db_config = DatabaseConfig()

# # Criar a string de conexão
# conn_string = db_config.get_connection_string()

# # Tentar conectar ao banco de dados
# try:
#     with psycopg2.connect(conn_string) as conn:
#         # Verificar se a conexão foi bem-sucedida
#         print("Status: Conexão realizada com sucesso.")
# except psycopg2.Error as e:
#     # Capturar e imprimir erros de conexão
#     print(f"Status: Erro na conexão. Mensagem: {e}")
# finally:
#     # Código que deve ser executado independentemente do resultado da conexão
#     print("Tentativa de conexão finalizada.")
