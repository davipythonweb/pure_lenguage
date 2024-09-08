"""class author"""
class Author:
    """tabela author"""
    def __init__(self, author_id, name, birthdate):
        self.author_id = author_id
        self.name = name
        self.birthdate = birthdate

    def __repr__(self):
        return f"<Author {self.name}>"
