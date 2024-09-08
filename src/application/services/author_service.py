
from src.infrastructure.repositories.author_repository import AuthorRepository

def get_author_by_id(author_id):
    """get em autores pelo id"""
    author = AuthorRepository.get_author_by_id(author_id)
    if not author:
        raise ValueError("Author not found")
    return author

def create_author(name, birthdate):
    """cria novos autores"""
    if not name:
        raise ValueError("Name is required")
    return AuthorRepository.insert_author(name, birthdate)
