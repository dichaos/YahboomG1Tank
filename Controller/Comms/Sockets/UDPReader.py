import struct
import socket
import abc
import threading

class UDPReader:

    def __init__(self, port):
        self.MAX_DGRAM = 2**16
        self.port = port
        self.loop = 1

    def dump_buffer(self, s):
        while True:
            seg, addr = s.recvfrom(self.MAX_DGRAM)
            if struct.unpack("B", seg[0:1])[0] == 1:
                break
    
    def start(self):
        self.loop = 1
        thread = threading.Thread(target=self.Loop)
        thread.daemon = True       
        thread.start()

    def Loop(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('', self.port))
        dat = b''
        self.dump_buffer(self.s)

        while self.loop == 1:
            seg, addr = self.s.recvfrom(self.MAX_DGRAM)
            if struct.unpack("B", seg[0:1])[0] > 1:
                dat += seg[1:]
            else:
                dat += seg[1:]
                self.Process(str(dat, 'utf-8'))
                dat = b''

    def stop(self):
        self.loop = 0
        self.s.close()

    @abc.abstractmethod
    def Process(self, value):
        pass