import socket
import time
from io import BytesIO
import abc

class SocketClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            self.socket.connect((self.ip, self.port))
            self.socket.setblocking(False)
        except:
            return False
            
        return True

    def send(self, value):
        self.socket.send((value+"\n").encode())

    def stop(self):
        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except (socket.error, OSError, ValueError):
            pass

        self.socket.close()
