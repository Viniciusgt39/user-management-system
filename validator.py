# validator.py

def validate_user(username: str, password: str, email: str) -> dict:
    """
    Valida os dados do usuário antes do registro.
    Retorna dict com 'valid' (bool) e 'errors' (list).
    """
    errors = []

    if len(username) < 3:
        errors.append("Username deve ter no mínimo 3 caracteres.")

    if len(password) < 6:
        errors.append("Senha deve ter no mínimo 6 caracteres.")

    if "@" not in email or "." not in email:
        errors.append("Email inválido.")
        
    return {"valid": len(errors) == 0, "errors": errors}