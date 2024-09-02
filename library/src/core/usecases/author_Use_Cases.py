from src.infrastructure.database.authorRepository import get_authors_repository, insert_authors_repository

def get_authors(callback):
    try:
        authors = get_authors_repository()
        callback(None, authors)
    except Exception as err:
        callback(err, None)

def insert_authors(name, birthdate, callback):
    try:
        author = insert_authors_repository(name, birthdate)
        callback(None, author)
    except Exception as err:
        callback(err, None)


# conexao com a tabela authors


# inserir dados na tabela authors