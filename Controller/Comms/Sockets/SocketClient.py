import socket
import time
from io import BytesIO
import abc

class SocketClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.loop = 1
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.connect((self.ip, self.port))
        self.socket.setblocking(False)

    def send(self, value):
        self.socket.send((value+"\n").encode())

    def stop(self):
        self.loop = 0
        self.socket.close()
