from auth import authenticate, hash_password
from validator import validate_user
from storage import save_user, get_user

def register_user(username, password, email):
    print(f"\n[SYSTEM] Registrando: {username}")
    
    result = validate_user(username, password, email)
    if not result["valid"]:
        print("Erros:", result["errors"])
        return False
    
    hashed = hash_password(password)
    # storage precisaria guardar senha também — extensão futura
    return save_user(username, email)

if __name__ == "__main__":
    register_user("joao", "senha123", "joao@email.com")
    register_user("jo", "123", "invalido")        # deve falhar na validação
    register_user("joao", "senha123", "joao@email.com")  # deve falhar no storage por duplicidade