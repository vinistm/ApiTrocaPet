import re
import jwt
from config import Config

def validar_senha(senha):
   
    if len(senha) < 6:
        return False
    if not re.search("[a-z]", senha):
        return False
    if not re.search("[A-Z]", senha):
        return False
    if not re.search("[0-9]", senha):
        return False
    if not re.search("[!@#$%^&*()_+=[\]{};':\"\\|,.<>/?]", senha):
        return False
    return True

def gerar_token_jwt(usuario_id):
    payload = {
        'usuario_id': usuario_id
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return token