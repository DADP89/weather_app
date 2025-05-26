import os
from dotenv import load_dotenv

def load_api_key():
    load_dotenv(dotenv_path=".env")
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("La variable de entorno 'API_KEY' no está definida en .env")
    return api_key