import os
from socket import socket, AF_INET, SOCK_STREAM

from dotenv import load_dotenv


class TCPServer:
    def __init__(self, ip: str, port: int, edit_message: callable = lambda x: x):
        self.ip = ip

        self.port = port

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(self.address)
        self.socket.listen(1)

        self.edit_message = edit_message

    @property
    def address(self) -> tuple:
        return self.ip, self.port

    def start(self):
        print(f"Server started on {self.address}")

        while True:
            connection, address = self.socket.accept()
            print(f"Connection from {address} established")

            while True:
                data = connection.recv(1024)
                print("Received data: ", data)

                if not data:
                    break

                res = self.edit_message(data.decode())

                connection.send(res.encode())

            connection.close()
            print(f"Connection with {address} closed")

    def close(self):
        self.socket.close()
        print("Server closed")


if __name__ == '__main__':
    load_dotenv()

    HOST = os.getenv("HOST")
    TCP_PORT = int(os.getenv("TCP_PORT"))


    def action(data: str) -> str:
        return data.upper()


    TCPServer(HOST, TCP_PORT, action).start()
