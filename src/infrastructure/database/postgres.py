
import psycopg2
from src.infrastructure.config.load_env import load_env

def get_db_connection():
    """conecta com o banco usando as variaveis de ambiente"""
    env = load_env()
    return psycopg2.connect(
        dbname=env['DB_NAME'],
        user=env['DB_USER'],
        password=env['DB_PASSWORD'],
        host=env['DB_HOST'],
        port=env['DB_PORT']
    )
