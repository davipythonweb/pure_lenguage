import os
import psycopg2
from dotenv import load_dotenv # pylint: disable=import-error

load_dotenv('../../.env')

conn_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'host': os.getenv('DB_HOST'),
    'password': os.getenv('DB_PASS'),
    'port': os.getenv('DB_PORT')
}

CONN_STRING = ' '.join([f"{key}='{value}'" for key, value in conn_params.items()])

try:
    with psycopg2.connect(CONN_STRING) as conn:
        print("Status: Conexão realizada com sucesso.")
except psycopg2.Error as e:
    print(f"Status: Erro na conexão. Mensagem: {e}")
finally:
    print("Tentativa de conexão finalizada.")
