from socket import socket, SOCK_STREAM, AF_INET


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
    client = TCPClient('localhost', 3500)
    print(client.send('hello'))

    client.close()
