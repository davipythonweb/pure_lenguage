import psycopg2
from psycopg2 import sql
from src.infrastructure.database.postgres import create_connection, call_procedure

# Cria a conexão com o banco de dados
client = create_connection()

def get_authors(callback):
    try:
        with client.cursor() as cursor:
            cursor.execute('SELECT * FROM "Authors";')
            results = cursor.fetchall()
            callback(None, results)
    except Exception as err:
        callback(err, None)

def insert_authors(name, birthdate, callback):
    try:
        call_procedure(client, 'insert_authors', [name, birthdate], callback)
    except Exception as err:
        callback(err, None)



# CHAMAR a FUNÇAO CONEXAO COM O BANCO

# conexao com a tabela authors


# inserir dados na tabela authors