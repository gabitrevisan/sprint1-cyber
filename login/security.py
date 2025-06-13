# sanitização e criptografia
import re
import bcrypt
import logging
from cryptography.fernet import Fernet
import os

# configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data/logs/security.log'),
        logging.StreamHandler()
    ]
)

def get_encryption_key():
    # gera/recupera chave de criptografia
    key_file = 'data/encryption.key'
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()

    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)
    return key

cipher_suite = Fernet(get_encryption_key())

def sanitize_input(input_str):
    # remove caracteres potencialmente perigosos
    if not input_str:
        return None
    return re.sub(r'[^\w@.+-]', '', input_str.strip())

def validate_username(username):
    # valida o formato do nome de usuário
    if not username or len(username) < 4:
        return False
    return bool(re.match(r'^[a-zA-Z0-9_@.+-]{4,30}$', username))

def validate_password(password):
    # valida a força da senha
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    return bool(re.search(r'[0-9]', password))

def encrypt_data(data):
    # criptografia de dados sensíveis
    try:
        if isinstance(data, str):
            data = data.encode()
        return cipher_suite.encrypt(data).decode()
    except Exception as e:
        logging.error(f"Erro ao criptografar dados: {e}")
        raise

def decrypt_data(encrypted_data):
    # descriptografia dos dados
    try:
        if isinstance(encrypted_data, str):
            encrypted_data = encrypted_data.encode()
        return cipher_suite.decrypt(encrypted_data).decode()
    except Exception as e:
        logging.error(f"Erro ao descriptografar dados: {e}")
        raise

def hash_password(password):
    # gera um hash seguro para senhas usando bcrypt
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(hashed_password, input_password):
    """Verifica se a senha corresponde ao hash"""
    return bcrypt.checkpw(input_password.encode(), hashed_password.encode())
