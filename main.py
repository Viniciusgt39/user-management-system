# main.py
from auth import authenticate
from validator import validate_user
from storage import save_user

def register_user(username, password, email):
    print(f"[SYSTEM] Iniciando registro de: {username}")

if __name__ == "__main__":
    register_user("joao", "senha123", "joao@email.com")