import os
from socket import socket, SOCK_STREAM, AF_INET

from dotenv import load_dotenv


class TCPClient:
    def __init__(self, ip: str, port: int):
        self.ip = ip

        self.port = port

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(self.address)

    @property
    def address(self) -> tuple:
        return self.ip, self.port

    def send(self, data: str) -> str:
        self.socket.send(data.encode())

        return self.socket.recv(1024).decode()

    def close(self):
        self.socket.close()


if __name__ == '__main__':
    load_dotenv()

    HOST = os.getenv("HOST")
    TCP_PORT = int(os.getenv("TCP_PORT"))

    client = TCPClient(HOST, TCP_PORT)
    print(client.send('hello'))

    client.close()
