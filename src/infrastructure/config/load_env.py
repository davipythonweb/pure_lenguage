
import os
from dotenv import load_dotenv

def load_env():
    """carrega variaveis de ambiente"""
    load_dotenv()
    return {
        'DB_USER': os.getenv('DB_USER'),
        'DB_PASSWORD': os.getenv('DB_PASS'),
        'DB_NAME': os.getenv('DB_NAME'),
        'DB_HOST': os.getenv('DB_HOST'),
        'DB_PORT': os.getenv('DB_PORT', '5432')
    }
