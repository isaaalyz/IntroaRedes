import socket

def start_server(host: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_socket.bind((host, port))

    print(f'Servidor UDP iniciado em {host}:{port}')

    while True:
        data, adress = server_socket.recvfrom(1024)
        message = data.decode('utf-8')
        print(f'[CLIENTE]: {message}') 

if __name__=='__main__':
    HOST = 'localhost'
    PORT = 9000

    start_server(HOST, PORT)