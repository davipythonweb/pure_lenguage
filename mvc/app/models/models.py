
import os
from dotenv import load_dotenv # pylint: disable=import-error

# Carregar variáveis de ambiente do arquivo .env
load_dotenv('../../.env')

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
