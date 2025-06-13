# Challenge XP – 2025.1
CyberSecurity

## NexTech
3ESPW – Eduardo Araujo (RM99758), Gabriela Trevisan (RM99500), Leonardo Bonini (RM551716) e Rafael Franck (RM550875)

- Acesso ao repositório no GitHub via https://github.com/gabitrevisan/sprint1-cyber

## Requirements
- bcrypt==4.0.1
- cryptography==39.0.1
- requests==2.28.2
- pyjwt==2.6.0
- bandit==1.7.4
- flake8==6.0.0

## How to run...
* Atenção! garanta que está no diretório correto [sp1_cyber] antes de iniciar a aplicação
* Aviso! os usuários "admin" e "gabi" já estão criados. Se tentar utilizar o login deles, com a senha errada, dará erro! Da mesma maneira, caso tente criar novos usuários com o mesmo login, também receberá uma mensagem de erro.
### Iniciando a aplicação
1) para fazer o cadastro do usuário, digite no terminal "python main.py register" 
2) para fazer o login, digite no terminal "python main.py login"
3) para fazer o logout, digite no terminal "python main.py logout --token [chave fornecida após o login]"


## Esse sistema conta com...
1. Sanitização e Validação de Entradas:
- Funções dedicadas para sanitização de inputs
- Validação rigorosa de nomes de usuário e senhas
- Remoção de caracteres potencialmente perigosos

2. Criptografia em Repouso:
- Uso de Fernet para criptografia dos dados no arquivo JSON
- Hashing de senhas com bcrypt
- Gerenciamento seguro de chaves de criptografia

3. Gerenciamento de Sessões:
- Tokens de sessão seguros usando secrets.token_hex()
- Tempo de expiração para sessões
- Atualização do tempo de atividade

4. Logs e Monitoramento:
- Registro detalhado de atividades
- Logs de segurança separados
- Detecção de atividades suspeitas

5. Validações de Segurança:
- Requisitos fortes para senhas
- Proteção contra brute force
- Tokens de API/sessão seguros
