# gerenciamento de sessões
import secrets
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class SessionManager:
    def __init__(self):
        self.active_sessions = {}
        self.session_timeout = timedelta(hours=1)

    def create_session(self, user_id):
        # cria uma nova sessão para o usuário
        session_token = secrets.token_hex(32)
        session_data = {
            'user_id': user_id,
            'created_at': datetime.now(),
            'last_activity': datetime.now()
        }
        self.active_sessions[session_token] = session_data
        logger.info(f"Nova sessão criada para o usuário {user_id}")
        return session_token

    def validate_session(self, session_token):
        # valida uma sessão existente
        if session_token not in self.active_sessions:
            logger.warning("Tentativa de acesso com token de sessão inválido")
            return False

        session_data = self.active_sessions[session_token]

        if datetime.now() - session_data['last_activity'] > self.session_timeout:
            self.end_session(session_token)
            logger.info(f"Sessão expirada para o usuário {session_data['user_id']}")
            return False

        session_data['last_activity'] = datetime.now()
        return True

    def end_session(self, session_token):
        # encerra uma sessão
        if session_token in self.active_sessions:
            user_id = self.active_sessions[session_token]['user_id']
            del self.active_sessions[session_token]
            logger.info(f"Sessão encerrada para o usuário {user_id}")

    def get_user_id(self, session_token):
        # obtém o ID do usuário associado à sessão
        if self.validate_session(session_token):
            return self.active_sessions[session_token]['user_id']
        return None

# instância global do gerenciador de sessões
session_manager = SessionManager()
