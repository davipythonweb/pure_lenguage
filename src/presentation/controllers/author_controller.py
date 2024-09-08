

import json
from src.application.services.author_service import get_author_by_id, create_author

class AuthorController:
    """class dos controllers"""
    @staticmethod
    def get_author_by_id(request, author_id):
        """get pelo id do autor"""
        try:
            author = get_author_by_id(author_id)
            return {'status': 200, 'data': author}
        except ValueError:
            return {'status': 404, 'message': 'Author not found'}
        except Exception as e:
            return {'status': 500, 'message': str(e)}

    @staticmethod
    def create_author(request):
        """create new author"""
        data = json.loads(request.body)
        try:
            author = create_author(data['name'], data['birthdate'])
            return {'status': 201, 'data': author}
        except ValueError as e:
            return {'status': 400, 'message': str(e)}
        except Exception as e:
            return {'status': 500, 'message': str(e)}
