# main.py  ← você vai editar isso aqui na branch
from auth import authenticate, hash_password
from validator import validate_user
from storage import save_user, get_user

def register_user(username, password, email):
    print(f"\n--- Registrando: {username} ---")
    
    result = validate_user(username, password, email)
    if not result["valid"]:
        print("Erros de validação:", result["errors"])
        return False
    
    saved = save_user(username, email)  # será alterado depois
    if saved:
        print("Registro concluído!")
    return saved