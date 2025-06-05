import socket

def send_message(host: str, port: int, message:str):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.sendto(message, (host, port))

if __name__=='__main__':
    HOST = 'localhost' #10.20.22.186 - end do professor
    PORT = 9000

while True:
    message = input ('Type your message: ').encode('utf-8')
    send_message(HOST, PORT, message)