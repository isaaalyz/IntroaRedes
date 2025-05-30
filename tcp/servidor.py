import socket

def start_server(host: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.binf((host, port))

    server_socket.listem(1)

    print(f'Servidor iniciado em {host}:{port}')
    client_socket, address = server_socket.accept()

    data = client_socket.recv(1024)
    message = data.decode('utf-8')
    print(message) 

if__name__=='__main__':
    HOST = 'locahoost'
    PORT = 8000

    start_server(HOST, PORT)