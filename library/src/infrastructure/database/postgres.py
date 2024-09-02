import psycopg2
from psycopg2 import sql
import os

def create_connection():
    """
    Função para conexão com o banco de dados PostgreSQL.
    """
    try:
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME')
        )
        print('Connected to PostgreSQL')
        return connection
    except Exception as err:
        print(f"Connection error: {err}")
        return None

def call_procedure(client, procedure_name, params, callback):
    """
    Função para chamar um procedimento armazenado no PostgreSQL.
    """
    try:
        with client.cursor() as cursor:
            query = sql.SQL("CALL {}({})").format(
                sql.Identifier(procedure_name),
                sql.SQL(', ').join(sql.Placeholder() * len(params))
            )
            cursor.execute(query, params)
            client.commit()
            callback(None, cursor.fetchall() if cursor.description else [])
    except Exception as err:
        client.rollback()
        callback(err, None)

# CRIAR FUNÇÂO PARA CONEXAO COM DATABASE