from socket import socket, SOCK_DGRAM, AF_INET


class UDPClient:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

        self.socket = socket(AF_INET, SOCK_DGRAM)

    @property
    def address(self) -> tuple:
        return self.ip, self.port

    def send(self, message: str) -> str:
        self.socket.sendto(message.encode(), self.address)
        data, address = self.socket.recvfrom(1024)

        return data.decode()

    def close(self):
        self.socket.close()


if __name__ == '__main__':
    client = UDPClient('', 5555)

    print(client.send("ciao"))

    client.close()
