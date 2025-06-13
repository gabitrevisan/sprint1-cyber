from socket import socket, AF_INET, SOCK_STREAM, gaierror

try:
    ip = input('Digite um alvo:\n> ')
    top_ports = [
        21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995,
        1723, 3306, 3389, 5900, 8080, 8009, 8180, 81, 300, 591, 593, 832, 981,
        1010, 1311, 2082, 2087, 2095, 2096, 2480, 3000, 3128, 3333, 4243, 4567,
        4711, 4712, 4993, 5000, 5104, 5108, 5800, 6543, 7000, 7396, 7474, 8000,
        8001, 8008, 8014, 8042, 8069, 8081, 8088, 8090, 8091, 8118, 8123, 8172,
        8222, 8243, 8280, 8281, 8333, 8443, 8500, 8834, 8880, 8888, 8983, 9000,
        9043, 9060, 9080, 9090, 9091, 9200, 9443, 9800, 9981, 12443, 16080,
        18091, 18092, 20720, 28017
    ]

    for port in top_ports:
        print(f'Escaneando porta {port}', end='\r')
        scanner = socket(AF_INET, SOCK_STREAM)
        scanner.settimeout(0.1)
        response = scanner.connect_ex((ip, port))

        if response == 0:
            print(f'Porta {port} aberta!')

except KeyboardInterrupt:
    print('Finalizado pelo usuário')
except gaierror:
    print('Host não identificado!')
