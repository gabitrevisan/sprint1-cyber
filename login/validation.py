# validação de entradas
import logging
from .security import sanitize_input, validate_username, validate_password

logger = logging.getLogger(__name__)

def validate_login_input(username, password):
    # valida entradas de login
    username = sanitize_input(username)
    password = sanitize_input(password)

    if not username or not password:
        logger.warning("Tentativa de login com campos vazios")
        return False, "Todos os campos são obrigatórios"

    if not validate_username(username):
        logger.warning(f"Formato de usuário inválido: {username}")
        return False, "Formato de usuário inválido"

    return True, None

def validate_registration_input(username, password):
    # valida entradas de registro
    valid, message = validate_login_input(username, password)
    if not valid:
        return valid, message

    if not validate_password(password):
        logger.warning("Senha não atende aos requisitos de segurança")
        msg = "A senha deve ter pelo menos 8 caracteres, incluindo maiúsculas, minúsculas e números"
        return False, msg

    return True, None
