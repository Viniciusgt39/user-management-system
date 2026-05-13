# auth.py
import hashlib

def hash_password(password: str) -> str:
    """Gera hash SHA-256 da senha."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username: str, password: str, stored_users: list) -> bool:
    """
    Verifica se username + senha batem com os dados armazenados.
    """
    hashed = hash_password(password)
    return any(
        u["username"] == username and u.get("password") == hashed
        for u in stored_users
    )