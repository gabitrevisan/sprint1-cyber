import argparse
from login.auth import register_user, login_user, logout_user

def main():
    parser = argparse.ArgumentParser(description='Sistema de Login NexTech')
    subparsers = parser.add_subparsers(dest='command', required=True)

    subparsers.add_parser('register', help='Registrar novo usuário')
    subparsers.add_parser('login', help='Fazer login')

    logout_parser = subparsers.add_parser('logout', help='Fazer logout')
    logout_parser.add_argument('--token', required=True, help='Token de sessão')

    args = parser.parse_args()

    if args.command == 'register':
        register_user()
    elif args.command == 'login':
        token = login_user()
        if token:
            print(f'Seu token de sessão: {token}')
    elif args.command == 'logout':
        logout_user(args.token)

if __name__ == '__main__':
    main()
