import os
from socket import socket, AF_INET, SOCK_DGRAM

from dotenv import load_dotenv


class UDPServer:
    def __init__(self, ip: str, port: int, edit_message: callable = lambda x: x):
        self.ip = ip
        self.port = port
        self.action = edit_message

        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(self.address)

    @property
    def address(self) -> tuple:
        return self.ip, self.port

    def start(self):
        print(f"Server started on {self.address}")

        while True:
            data, address = self.socket.recvfrom(1024)
            print("Received data: ", data, "from", address)

            res = self.action(data.decode())

            self.socket.sendto(res.encode(), address)

    def close(self):
        self.socket.close()
        print("Server closed")


if __name__ == '__main__':
    load_dotenv()

    HOST = os.getenv("HOST")
    UDP_PORT = int(os.getenv("UDP_PORT"))


    def action(message: str) -> str:
        return message.upper()


    UDPServer(HOST, UDP_PORT, action).start()
