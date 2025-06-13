# lógica de autenticação
import json
import os
from getpass import getpass
import logging
from .security import encrypt_data, decrypt_data, hash_password, verify_password
from .validation import validate_login_input, validate_registration_input
from .session import session_manager

logger = logging.getLogger(__name__)

USER_DATA_FILE = 'data/contas.json'

def load_users():
    # carrega os usuários do arquivo JSON
    try:
        if not os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'w') as f:
                json.dump({}, f)
            return {}

        with open(USER_DATA_FILE, 'r') as f:
            data = json.load(f)
            return {
                user: decrypt_data(pwd) if pwd.startswith('gAAAA') else pwd
                for user, pwd in data.items()
            }
    except Exception as e:
        logger.error(f"Erro ao carregar usuários: {e}")
        return {}

def save_users(users):
    # salva os usuários no arquivo JSON
    try:
        encrypted_users = {
            user: encrypt_data(pwd) 
            for user, pwd in users.items()
        }

        with open(USER_DATA_FILE, 'w') as f:
            json.dump(encrypted_users, f, indent=2)
    except Exception as e:
        logger.error(f"Erro ao salvar usuários: {e}")
        raise

def register_user():
    # registra um novo usuário
    username = input('Digite o nome de usuário:\n> ')
    password = getpass('Digite a senha: ')

    valid, message = validate_registration_input(username, password)
    if not valid:
        print(message)
        return False

    users = load_users()
    if username in users:
        print('Este usuário já existe')
        logger.warning(f"Tentativa de registrar usuário existente: {username}")
        return False

    users[username] = hash_password(password)
    save_users(users)
    logger.info(f"Novo usuário registrado: {username}")
    print('Usuário registrado com sucesso!')
    return True

def login_user():
    # autentica um usuário
    username = input('Digite o seu login:\n> ')
    password = getpass('Digite a sua senha: ')

    valid, message = validate_login_input(username, password)
    if not valid:
        print(message)
        return None

    users = load_users()
    if username not in users or not verify_password(users[username], password):
        print('Usuário ou senha incorretos!')
        logger.warning(f"Tentativa de login falha para o usuário: {username}")
        return None

    session_token = session_manager.create_session(username)
    logger.info(f"Login bem-sucedido para o usuário: {username}")
    print('Login realizado com sucesso!')
    return session_token

def logout_user(session_token):
    # encerra a sessão do usuário
    session_manager.end_session(session_token)
    print('Logout realizado com sucesso!')
