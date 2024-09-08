
from src.infrastructure.database.postgres import get_db_connection

class AuthorRepository:
    """classes com as querys no database"""
    @staticmethod
    def get_author_by_id(author_id):
        """query no database pelo id"""
        query = 'SELECT id, name, birthdate FROM "Authors" WHERE id = %s'
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (author_id,))
                return cursor.fetchone()

    @staticmethod
    def insert_author(name, birthdate):
        """query no database para inserir novo aoutor"""
        query = 'INSERT INTO "Authors" (name, birthdate) VALUES (%s, %s)'
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (name, birthdate))
                conn.commit()
