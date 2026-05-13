# storage.py
import json
import os

STORAGE_FILE = "users.json"

def _load_users() -> list:
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)
    
def save_user(username: str, email: str) -> bool:
    """Salva usuário no arquivo JSON. Retorna False se já existir."""
    users = _load_users()
    
    if any(u["username"] == username for u in users):
        print(f"Erro: usuário '{username}' já existe.")
        return False
    
    users.append({"username": username, "email": email})
    
    with open(STORAGE_FILE, "w") as f:
        json.dump(users, f, indent=2)
    
    print(f"Usuário '{username}' salvo com sucesso.")
    return True

def get_user(username: str) -> dict | None:
    """Busca usuário pelo username."""
    users = _load_users()
    return next((u for u in users if u["username"] == username), None)